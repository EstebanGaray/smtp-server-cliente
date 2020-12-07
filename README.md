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
sudo docker run -it ID \
ex: sudo docker run -it 9c1bf33e1f16 \
algunos comandos basicos para usar el cliente \
./smtp-cli--verbose --server IP-HOST:puerto(25 por defecto) \
./smtp-cli--verbose --server IP-HOST:puerto(25 por defecto) --from example@gmail.com --to my@haraka.test --subject example --body-plain "texto" \
--to tiene que ser hacia un mail terminado en @haraka.test \
esto se puede modificar agregando a la lista de host que mails quiere haceptar \
enlace a video de muestra:https://youtu.be/eLVpkrMywdc \
enlace a video en que se editan paquetes:https://youtu.be/HqBmPB6lfjs
enlace a video de metricas: https://youtu.be/_y58YE8BWXo
enlace a video snort:https://youtu.be/N7KlsCaqTzg
