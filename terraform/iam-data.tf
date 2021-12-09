data "aws_iam_policy_document" "role_policy" {
  statement {
    sid    = 1
    effect = "Allow"

    actions = [
      "sts:*",
    ]

    resources = [
      "${aws_iam_role.role.arn}",
    ]
  }
}
