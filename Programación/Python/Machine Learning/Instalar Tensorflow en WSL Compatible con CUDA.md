En este instructivo, explicare paso a paso los pasos que me han funcionado para poder hacer funcionar WSL2 con CUDA, ya que las instrucciones que vienen en internet pueden ser un poco incompletas o te pueden conducir a un callejón sin salida. Cabe destacar que se contempla que ya tengas funcional tu maquina linux funcionando con WSL.

## Requisitos

Para poder instalar `tensorflow[and-cuda]` y que funcione correctamente, debemos cumplir con los siguientes requisitos en nuestra maquina linux:

- Contar con los Drivers de Envidia en la Maquina Host
- Instalar CUDA Toolkit
- Instalar cuDNN
- Cargar Variable de Entorno
- (Opcional) Tener `anaconda`

A continuación, cubriré cada requisito paso a paso para poder guiarte exitosamente:

### 1. Instalar CUDA Toolkit

Para instalar cuda toolkit debemos consultar la version apta para nuestra distribucion de linux: [CONSULTAR AQUI](https://developer.nvidia.com/cuda-downloads?target_os=Linux)

Cuando terminemos de elegir nuesta distribucion, la pagina nos dara los comandos necesarios para instalarlo, ejemplo:

```shell
wget https://developer.download.nvidia.com/compute/cuda/12.6.2/local_installers/cuda-repo-debian12-12-6-local_12.6.2-560.35.03-1_amd64.deb
sudo dpkg -i cuda-repo-debian12-12-6-local_12.6.2-560.35.03-1_amd64.deb
sudo cp /var/cuda-repo-debian12-12-6-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo add-apt-repository contrib
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-6
```

Sin embargo, en mi caso personal, al hacer el segundo comando (`sudo dpkg -i cuda-repo-debian12-12-6-local_12.6.2-560.35.03-1_amd64.deb`) me solicitaba ejecutar un comando para continuar satisfactoriamente con la instalacion, es el equivalente al comando de abajo (`sudo cp /var/cuda-repo-debian12-12-6-local/cuda-*-keyring.gpg /usr/share/keyrings/`) el cual no me funciono, por lo que resulta que hay que ejecutar el comando y nuevamente intentar el segundo comando.

Cuando hagamos eso, ya podemos saltar directamente a un `sudo apt update` y finalmente el comando `sudo apt-get -y install cuda-toolkit-12-6`.

### 2. Instalar cuDNN

Igualmente que el paso anterior, debemos entrar al siguiente link y elegir la configuracion de nuestro sistema operativo: [AQUI](https://developer.nvidia.com/cudnn-downloads?target_os=Linux)

Una vez descargado, tendremos los comandos a ejecutar como en el paso anterior:

```shell
wget https://developer.download.nvidia.com/compute/cudnn/9.4.0/local_installers/cudnn-local-repo-debian12-9.4.0_1.0-1_amd64.deb
sudo dpkg -i cudnn-local-repo-debian12-9.4.0_1.0-1_amd64.deb
sudo cp /var/cuda-repo-debian12-9-4-local/cudnn-*-keyring.gpg /usr/share/keyrings/
sudo add-apt-repository contrib
sudo apt-get update
sudo apt-get -y install cudnn
```

Es curioso porque me paso exactamente los mismo con este paquete, me pedia ejecutar un comando para continuar, lo ejecutamos y nuevamente probamos el segundo comando, hacemos un `sudo apt update` y finalmente un `sudo apt-get -y install cudnn`.

### 3. Cargar Variables de Entorno

Para cargar las variables de entorno solo basta con saber si estamos usando `zsh` o `bash`, para cada caso:

- BASH:
```shell
echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc source ~/.bashrc
```

- ZSH:
```shell
echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.zshrc echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.zshrc source ~/.zshrc
```

## 4. Probar Instalacion

Si todo salio bien y como deberia, debemos tener dos comandos que nos responden correctamente con unas salidas similares:

```shell
nvcc --version
```

![[nvcc.png]]

```shell
nvidia-smi
```

![[nvidia-smi.png]]

## 5. Configurar Entorno

Para este caso, usare anaconda, puedes descargarlo en la pagina [oficial](https://www.anaconda.com/download/success), basta con un `bash .Anaconda3-2024.06-1-Linux-x86_64.sh` para instalarlo, solo dile `yes` y `yes` cuando termine.

Primero, creamos nuestro entorno virtual:

```shell
conda create --name CUDA python=3.11
```

Le damos al enter y cuando termine tendremos el entorno, ahora toca activarlo:

```shell
conda activate CUDA
```

Finalmente, ahora necesitamos instalar `tensorflow` con compatibilidad con CUDA:

```shell
pip install 'tensorflow[and-cuda]'
```

Le decimos que si y esto bastara para que podamos probar el comando:

```shell
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```


> [!Warning] NUMA
> Puede que nos salten varias alertas, por ejemplo, nos puede decir algo como: `I0000 00:00:1728210504.136460   20946 cuda_executor.cc:1001] could not open file to read NUMA node: /sys/bus/pci/devices/0000:08:00.0/numa_node Your kernel may have been built without NUMA support.` Sin embargo, podremos notar que al momento de entrenar un modelo, a pesar de las advertencias tendremos el aviso: `2024-10-06 04:28:39.716586: I external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:531] Loaded cuDNN version 8907` lo cual significa que efectivamente se esta usando la GPU par a el entrenamiento.

Cuando hagamos un entrenamiento de modelo, podremos notar que efectivamente el uso de la GPU aumenta, por lo que podremos saber que hemos hecho todo el proceso bien, adicional a esto, podemos usar `pip install tensorRT` y posteriormente un `export LD_LIBRARY_PATH=<TensorRT-${version}/lib>:$LD_LIBRARY_PATH` por si nos salta un aviso de esa biblioteca faltante, ademas, puede mejorar la latencia en algunas tarjetas graficas.

```shell
python3 -c "import os; os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'; import tensorflow as tf; print('Num GPUs Available: ', len(tf.config.list_physical_devices('GPU')))"
```