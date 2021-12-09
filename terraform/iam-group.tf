resource "aws_iam_group" "group" {
  name = "${var.environment}-group"
}

resource "aws_iam_group_policy_attachment" "group-attach" {
  group      = aws_iam_group.group.name
  policy_arn = aws_iam_policy.role_policy.arn
}
