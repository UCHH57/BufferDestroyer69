# [BufferDestroyer69]

## Les_buffer_overflow

En informatique, un dépassement de tampon ou débordement de tampon (en anglais, buffer overflow) est un bug par lequel un processus, lors de l'écriture dans un tampon, écrit à l'extérieur de l'espace alloué au tampon, écrasant ainsi des informations nécessaires au processus. (cf. Wikipedia)  
Afin d'expliquer les buffers overflow, nous allons tout d'abord revoir la mémoire des programmes informatiques.
Nous prendrons comme exemple des programmes utilisant l'architecture i386 (Intel Architecture, 32-bits).
## memory segmentation - IA32 Architecture
```
                              Memory
                                                 Higher Memory Addresses
                 +-----------------------------+
                 |        kernel space         |
  [1] 0xc0000000 +-----------------------------+
                 |~~~~~~~ random offset ~~~~~~~|
                 +-----------------------------+
                 | |                           |
                 | v          Stack            |
                 +-----------------------------+
                 | / / / / / / / / / / / / / / |
                 +-----------------------------+
                 | |                           |
                 | v      Shared memory        |
                 +-----------------------------+
                 | / / / / / / / / / / / / / / |
             brk +-----------------------------+
                 | ^                           |
                 | |          Heap             |
       Start brk +-----------------------------+
                 |~~~~~~~ random offset ~~~~~~~|
                 +-----------------------------+
                 |             bss             |
                 +-----------------------------+
                 |            data             |
                 +-----------------------------+
                 |            text             |
  [2] 0x08048000 +-----------------------------+
                 | / / / / / / / / / / / / / / |
      0x00000000 +-----------------------------+
                                                  Lower Memory Addresses
```

Il y a deux principaux types de buffer overflow, ciblant chacun une zone mémoire différente,
les Stack based Buffer Overflow (SBOF) et les Heap based Buffer Overflow (HBOF).  
Leur exploitation est similaire seul la zone mémoire change.  
Pour expliquer la faille, nous parlerons principalement des SBOF.  
Prenons pour exemple le code suivant:

```c
int auth()
{
	int isAdmin = 0;
	buff[24];

	read(1, buff, 100);
	if (strcmp(passwd, buf) == 0)
		isAdmin = 1;

	return (isAdmin);
}
```

Imaginons alors que l'utilisateur entre 31 'a'.
## Stack avant l'appel de 'read'
```
                              Stack
                                                 Higher Memory Addresses
                 +-----------------------------+
                 | / / / / / / / / / / / / / / |
                 +-----------------------------+
                 |        sauvegarde EIP       |
                 +-----------------------------+
                 |        sauvegarde EBP       |
             EBP +-----------------------------+
                 |           isAdmin           |
                 +-----------------------------+
                 |            buff             |
             ESP +-----------------------------+
                                                  Lower Memory Addresses
```
## Stack apres l'appel de 'read'
```
                              Stack
                                                 Higher Memory Addresses
                 +-----------------------------+
                 | / / / / / / / / / / / / / / |
                 +-----------------------------+
                 |        sauvegarde EIP       |
                 +-----------------------------+	^
                 |        sauve... aaa         | 	|
             EBP +-----------------------------+	|  sens de
                 |            aaaa             |	|  l'ecrasement.
                 +-----------------------------|	|
                 |  aaaaaaaaaaaaaaaaaaaaaaaa   |	|
             ESP +-----------------------------+
                                                  Lower Memory Addresses
```
le buffer n'étant prévu que pour accueillir 24 octets, il y a donc eu un débordement, les variables qui se trouvaient au-dessus de la variable 'buff' dans la Stack ont donc été écrasées.  
Ici par exemple il y a deux scénarios d'attaque,
- Le premier est d'écraser la variable isAdmin
  pour faire croire au programme que le bon mot de passe a été entré.
- Le second est d'écraser l'adresse de retour (la sauvegarde du registre EBP)
  afin de rediriger le flux d'exécution du programme à une adresse souhaitée (un shellcode par ex.).

## Le_projet
Le but du projet est de simplifier l'exploitation de buffer overflow.  
Il sera réalisé en Python3 et se présentera sous la forme d'un interactive shell.

## Fonctionalités

### Features principales
- définir si l'argument est en paramètre (argc) ou lu (lu par défaut)
- changer le shellcode par défaut (par défaut system("/bin/sh") )
- sauter dans une fonction ou à une adresse précise.
- set un shellcode en variable d'environnement et de récupérer son adresse.
- set une valeur précise dans une variable
- lancer un shellcode
- appeler la fonction system avec l'argument choisi (ret2libc)
- effectuer du nopSpread. (payload de type: l'adresse possible et approximative du shellcode + beaucoup de Nop + le shellcode)
- lancer avec son propre payload. (pour faire du Return Oriented Programming (ROP) ou dans d'autres cas complexes)

### Features annexes
- tester si l'ASLR est activé
- lister les fonctions
- lancer gdb
- lister les fichiers
- désassembler une fonction

# Comment contribuer ?

le programme est pensé pour pouvoir ajouter de nouvelles commandes très facilement.

## Premier étape

Créer votre .py dans le dossier src/commands/

## Deuxième étape

Importer la class Command qui se trouve dans src/Command.py

`from src.Command import Command`

Implementer la class command et override la function set_option

```python
class ChangeShellcodeCommand(Command):
    command = "cshc"
    usage = "[new shellcode]"

    def set_option(self, option, cmd):
        option.shellcode = cmd[1]
```

option est une structure de donnée qui vas etre donne à l'executeur de commands
aprés l'appel de votre command c'est avec celle-ci que vous allez pouvoir fair executer vos commands offensive. (cf. src/Option.py)

## Troisème étape

Importer votre commande dans le src/CommandHandler.py

`from .commands.ChangeShellcodeCommand import ChangeShellcodeCommand`

puis ajoutez le point d'entrée de votre command dans la function init_all_command

`self.commands.append(ChangeShellcodeCommand())`

## Quatrième étape

Test
