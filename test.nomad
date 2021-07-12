job "docs" {
  datacenters = ["dc1"]

  group "example" {
    
    network {
      port "http" {
        static = "1115"
      }
    }
    task "server" {
      driver = "docker"

      config {
        image = "msamaheen/app1:latest"
        ports = ["http"]
      }
    }

    task "kondara" {
      driver = "exec"
      config {
        command = "/bin/bash"
        args = ["-c", "docker network create mynetwork"]
      }
    }

  }  
}
