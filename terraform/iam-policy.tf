resource "aws_iam_policy" "role_policy" {
  name   = "${var.environment}-policy"
  policy = data.aws_iam_policy_document.role_policy.json
}
