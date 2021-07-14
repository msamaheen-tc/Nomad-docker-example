job "exercise-deploy6" {
  datacenters = ["dc1"]

  group "exercise-group" {
    task "app1-task" {
      driver = "docker"
      config {
        image = "mshaloditc/nomad-exercise:app1"
        ports = ["app1-port"]
      }

      template {
        data = <<EOF
TARGET_PASSWORD={{ with secret "secret/mysecret" }}{{ .Data.data.password }}{{ end }}
EOF
        destination = "secrets/passwords.txt"
        env = true
      }
    }

    task "app2-task" {
      driver = "docker"
      config {
        image = "mshaloditc/nomad-exercise:app2"
        ports = ["app2-port"]
      }

      template {
        data = <<EOF
TARGET_PASSWORD={{ with secret "secret/mysecret" }}{{ .Data.data.password }}{{ end }}
EOF
        destination = "secrets/passwords.txt"
        env = true
      }
    }

    network {
      mode = "bridge"
      port "app1-port" {
        static = "1115"
      }
      port "app2-port" {
        static = "1116"
      }
    }
  }
}