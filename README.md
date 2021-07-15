1- run Vault locally
run: vault server -dev

2- open new terminal then
run: sudo -i

3- set environment variables
run: export VAULT_ADDR='http://127.0.0.1:8200'
run: export VAULT_TOKEN="s.rt2hBodMhtmKDvWrx4icKm93"   # replace the token with the one you have on vault logs when you run the server

4- Download the policy and write it to vault server
run: curl https://nomadproject.io/data/vault/nomad-server-policy.hcl -O -s -L
run: vault policy write nomad-server nomad-server-policy.hcl

5- Download the token role and write it to vault server
run: curl https://nomadproject.io/data/vault/nomad-cluster-role.json -O -s -L
run: vault write /auth/token/roles/nomad-cluster @nomad-cluster-role.json

6- run Nomad locally
run: nomad agent -dev

7- go to localhost:8200 and add a secret called 'mysecret', and put password attribute in it with some value

8- run Consul locally
run: consul agent -dev

9- expose port 8500 to internet via ngrok

10- replace the consul host with the ngrok you get in app1/main.py file

11- build and push the images to your docker hub repo

12- replace the image source in deploy.nomad with yours

13- copy deploy.nomad contents and run a new job on nomad (localhost:4646)

14- to verify, go to localhost:1115, localhost:1115/info, localhost:1115/secret