resource "aws_s3_bucket" "aws_s3_bucket_portal" {
  bucket = "ilan0805.com"
  acl    = "public-read"

  policy = <<EOF
{
  "Statement": [
    {
      "Sid": "PublicReadForGetBucketObjects",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::ilan0805.com/*"
    }
  ]
}
EOF

  website {
    index_document = "index.html"
    error_document = "index.html"
  }
}

# upload root files to the bucket
resource "aws_s3_bucket_object" "website_files" {
  for_each = fileset("upload", "**/*.*")
  bucket = aws_s3_bucket.aws_s3_bucket_portal.bucket
  key = replace(each.value, "upload", "")
  source = "upload/${each.value}"
  content_type = "text/html"
}