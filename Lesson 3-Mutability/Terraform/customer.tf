#
# ------- Cloud Provider -------
#

provider aws {
    access_key  = "${var.access_key}"
    secret_key  = "${var.secret_key}"
    region      = "${var.region}"
}

#
# ------- Networking -------
#

resource "aws_security_group" "intro-to-sre-nsg" {
  name        = "intro-to-sre-us-west-2"
  description = "Allow all inbound traffic"
  vpc_id      = "${var.vpc}"

  # allow communication from inside the sg
  ingress {
  from_port = 0
  to_port = 0
  protocol = "-1"
  self = true
  description = "allow traffic from inside the SG"
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
}

#
# ------- Postgres DB Instance -------
#

resource "aws_db_instance" "intro-to-sre-postgres-prod1" {
  allocated_storage    = 60
  storage_type         = "gp2"
  engine               = "postgres"
  engine_version       = "9.6"
  instance_class       = "db.t2.micro"
  identifier           = "intro-to-sre"
  username             = "pgadmin"
  password             = "${var.db_password}"
  vpc_security_group_ids = ["${aws_security_group.intro-to-sre-nsg.id}"]

  backup_retention_period = 7

}
