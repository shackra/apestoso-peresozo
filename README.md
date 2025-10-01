# Apestoso Perezoso: graba entradas de controles y los reproduce en GNU/Linux

Graba y reproduce entradas de control, ideal para granjear (*farmear*) Runas en Elden Ring de manera *desatendida.

## Configuración previa

Por favor asegúrese que su usuario es parte del grupo `input`, use `groups` en una terminal para saber esa información. Si no es parte del grupo `input`, agregue su usuario. Para usuarios de NixOS todo lo que debe hacer es modificar `users.users.su_usuario_aqui.extraGroups`:

```nix
users.users.su_usuario_aqui.extraGroups = [ "input" ];
```

Luego de reconstruir su sistema operativo con la nueva configuración, debe reiniciar para estar seguro que los cambios han sido aplicados. Ahora el comando `groups` deberia mostrar que ud es parte del grupo `input`.

## Instalación

### Para usuarios que no usan Nix o NixOS

> [!NOTE]
> Por hacer...

### Para usuarios de Nix o NixOS con Flakes

Para instalar si se es usuario de Nix/NixOS con Flakes, debe agregar la entrada a su archivo `flake.nix`, adapte según corresponda:

```nix
# ... (significa que ud puede tener código Nix y se omite para brevedad)
inputs = {
  apestoso-peresozo = {
    url = "github:shackra/apestoso-peresozo";
	inputs.nixpkgs.follows = "nixpkgs";
  };
}
# ...
```

y luego se declara la instalación del paquete a nivel del sistema:

```nix
outputs = { ..., apestoso-peresozo }:
# ...
{
  # ...
  nixosConfiguration.cambiar_por_su_maquina = nixpkgs.lib.nixosSystem {
    modules = [
	  # ...
	  { environment.systemPackages = [ apestoso-peresozo.packages."x86_64-linux".default ]; } # x86_64-linux porque se asume que esta usando GNU/Linux
	];
	  # ...
  };
  # ...
}
```

¡Y regenere su sistema operativo!

## Como usar

1. Conecte su control por medio de USB a su computadora
2. Averigüe cual es el descriptor, use `ls -l /dev/input/by-id/`

```
~ ls -l /dev/input/by-id/

Permissions Size User Date Modified Name
lrwxrwxrwx     - root 30 sep 15:37   usb-Corsair_CORSAIR_SLIPSTREAM_WIRELESS_USB_Receiver_CFAAF05119F68BFA-event-if04 -> ../event2
...
lrwxrwxrwx     - root 30 sep 17:34   usb-Microsoft_Controller_3039565830323137303432323337-event-joystick -> ../event26
lrwxrwxrwx     - root 30 sep 17:34   usb-Microsoft_Controller_3039565830323137303432323337-joystick -> ../js1
...
```

En mi caso (un XBox One) el control sería `event26`, y su ubicación absoluta `/dev/input/event26`. Tenga en cuenta que este identificador puede cambiar entre reinicios.

3. Para grabar, en la terminal invoque `apestoso /dev/input/event26 ~/grabacion.json`, nótese que ud debe usar la ubicación absoluta del control en su sistema ¡si no ve texto durante la grabación se equivoco de dispositivo!. También debe especificar donde se guardará la grabación, para este ejemplo elegí mi carpeta personal (`~`).

> [!CAUTION] 
> Se recomienda que el juego este listo antes de empezar a
> grabar los comandos del control.

4. Para reproducir, en la terminal invoque `peresozo ~/grabacion.json`, asegúrese de tener el juego listo porque debe tener el foco o de otro modo el juego no tendrá noticia de los comandos que esta reproduciendo, tiene un tiempo de gracia de 5 segundos para realizar el cambio de foco de la terminal al juego.

5. Entre repetición de la grabación hay un tiempo de gracia de 10 segundos para detener el juego, cambiar el foco a la terminal y cancelar la reproducción de los comandos grabados. La reproducción continuara de manera indefinida —sin importar si todo marcha como se espera dentro del juego—.

6. (Opcional y aclaración para la palabra "desatendida") Supervise la reproducción de la grabación por un tiempo prudencial para tener completa seguridad que todo trabaja como se espera. Si es así, puede dedicarse a otras cosas mientras `peresozo` *granjea* por ud.

> [!CAUTION]
> NO ME HAGO RESPONSABLE POR EL MAL USO DE LOS SCRIPTS
> PROVISTOS EN ESTE PROYECTO.

