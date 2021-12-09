resource "aws_iam_group_membership" "team" {
  name = "tf-${var.environment}-group-membership"

  users = [
    aws_iam_user.ci_user_one.name,
  ]

  group = aws_iam_group.group.name
}

resource "aws_iam_user" "ci_user_one" {
  name = "${var.environment}-user"
}

