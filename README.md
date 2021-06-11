## DESPLIEGUE DE UNA APLICACION EN PYTHON Y UNA BASE DE DATOS REDI CON KUBERNETES

### Pasos para desplegar la applicacion:

Los pasos a seguir y los paquetes descargados son ejemplo para un entorno local, especialmente usando una maquina ubuntu o linux.
Las herramientas necesarias son:
* Kubernets (Minikube y kubectl)
* Ansible
* Docker

-  Si la aplicacion se va a desplegar en un entorno local,como se va a utilizar kubernets es importante tener el software descargado en el computador.
Para esto hay que tener un cluster local para poder desplegar la aplicacion. Hay varias opciones como micrk8s, minikube, etc. 
Los archivos que que vamos a utilizar estan en formato yml, para esto debe instalar ansible. En este caso, ilustramos la manera para hacerlo en una maquina ubunut
pero puede seguir los pasos si tiene otra maquina aqui :

https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

Primero, instale el paquete ansible en su equipo, ya que desplegaremos archivos en este formato:

```shell
$sudo apt update
$sudo apt install ansible
```


-  Ahora si,instale kubectl: Aqui encontrara los pasos exactos por Kubernetes para diferenetes maquinas : https://kubernetes.io/es/docs/tasks/tools/install-kubectl/
Para este caso,usaremos estos comandos para una maquina ubuntu:
$ snap install kubectl --classic
$ kubectl version --client

- A continuacion , debe instalar una herramienta que le permite tener un cluster en su maquina host, en este caso usaremos minikibue.
Aqui podra encontrar los pasos exactos para instalarlo en una maquina diferente: https://minikube.sigs.k8s.io/docs/start/
Para este caso de ilustracion, usaremos la instalacion para una maquina ubuntu:
```shell
$ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
$ sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
Ahora, para poder inicializar el cluster en su maquina , debe ejecutar el siguiente comando:
```shell
$ minikube start
```
Verifique que se instalo bien realziando el comando:
```shell
$ kubectl get po -A
```

-  A continuacion, se desplegara la aplicacion:
Descargue este repositorio https://github.com/sebastianRebolledo/parcial3-distribuidos-k8s
entre a la carpeta kubernets:
```shell
$ cd kubernets
```

Estando alli, debe ejecutar los pods. Primero, despligue los pods de la base de datos asi:
```shell
$ kubectl apply -f database-deployment.yml
```
Despues despliegue el servicio de la base de datos, la cual nos permitira conectarnos con la aplicacion.
```shell
$ kubectl apply -f database-service.yml
```

Ahora, despliegue la aplicacion de la misma manera
```shell
$ kubectl apply -f  app-deployment.yml
```
Ahora despliegue el servicio de la aplicacion, el cual buscara el servicio de la base de datos que ya fue desplegado en el paso anterior.
```shell
$ kubectl apply -f  app-service.yml
```

Verifique que los servicios estan corriendo asi:
```shell
$ kubectl get services
```
Debe encontrar los dos servicios que acabo de desplegar con los nombres app-service y redis con su respectiva IP
Verifique que los pods esten corriendo asi:
```shell
$ kubectl get pods
```
Debe encontrar cuatro pods , dos pertenecientes al la base de datos y dos de la aplicacion con nombre db-deployment y para la base de datos app-deployment

Ahora ejecute el comando :
```shell
$ minikube service app-service
```

Se le abrira una ventana emergente y encontrara el mensaje Hello World k8s parcial distribuidos


## ¿ QUE HARIA SI PUSIERA EN PRODUCCION ESTA APLIACION CON KUBERNETS Y COMO PODRIA MEJORARLO SI TUVIERA MAS TIEMO ?

Para poner en produccion este servicio podria utilizar Helm, el cual es una herramienta que permite adminsitrar y desplegar nuestro cluster de una manera mas facil
y mas organziada, evitando realizar los comandos manualmente que anteriormente describimos. Otra opcion seria utilizar plugins de Ansible como community k8s, el cual
facilita de igual forma el despliegue del cluster en un ambiente de produccion evitando introducir comonados manualmente.

Otro que podria mejorar seria si esto fuera llevado a un ambiente cloud, podria utilizar difernetes proveedores pero para este caso utilizaria AWS. AWS tiene un servicio llamado
EKS (Elastic Kubernets Services) el cual nos permite desplegar cluster de kubernets y manejar una cantidad de nodos a nuestra disposicion. 
