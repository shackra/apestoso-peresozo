# Apestoso Perezoso: graba entradas de controles y los reproduce en GNU/Linux

Graba y reproduce entradas de control, ideal para granjear (farmear) Runas en Elden Ring de manera desatendida.

## Configuración previa

Por favor asegurese que su usuario es parte del grupo `input`, use `groups` en una terminal para saber esa información. Si no es parte del grupo `input`, agregue su usuario. Para usuarios de NixOS todo lo que debe hacer es modificar `users.users.su_usuario_aqui.extraGroups`:

```nix
users.users.su_usuario_aqui.extraGroups = [ "input" ];
```

Luego de reconstruir su sistema operativo con la nueva configuración, debe reiniciar para estar seguro que los cambios han sido aplicados. Ahora el comando `groups` deberia mostrar que ud es parte del grupo `input`.

## Instalación
