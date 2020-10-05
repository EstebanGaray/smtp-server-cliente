# smtp-server-cliente
servidor creado a partir de haraka https://github.com/haraka/Haraka \
cliente creado apartir de smpt-cli https://github.com/mludvig/smtp-cli \
Ejecutar server: \
construya el dockerfile \
sudo docker build . \
una vez termine aranque el server con \
sudo docker run -ti -p 25:25 ID \
Ejecutar cliente: \
construya el dockerfile \
sudo docker build .una vez termine ya puede usar el cliente con: \
sudo docker run -it ID --verbose --server IP-HOST:25 \
o \
sudo docker run -it --net=host ID --verbose --server localhost:25 \
ex: \
sudo docker run -it --net=host 9c1bf33e1f16 --verbose --server localhost:25 --from example@gmail.com --to my@haraka.test --subject example --body-plain "texto" \
--to tiene que ser hacia un mail terminado en @haraka.test \
esto se puede modificar agregando a la lista de host que mails quiere haceptar \
enlace a video de muestra:https://youtu.be/eLVpkrMywdc
