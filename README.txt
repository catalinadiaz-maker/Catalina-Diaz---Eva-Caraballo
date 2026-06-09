Nombre: VACA tienda online.
Problema: El calculo de descuento en una tienda online durante el black friday.
Usuario: Compradores online.
Funcionaliades: Registrar productos de una tienda online, dividirlos en categorias y calcular su precio final tras aplicar un descuento.
Conceptos: Encapsulamiento: se utilizo para poner como un atributo privado y proteger la información de la clase madre (self,nombre, precio, stock) para que funcione un encapsulamiento se utiliza __ antes de el atributo
           Herencia: La clase madre Producto le hereda a sus clases hijas (ropa, electrodomestico, juguetes, limpieza) sus atributos (nombre, precio, stock)
           Abstraccion: Con la abstracción logramos que el metodo en nuestro caso (def descuento(self):) se aplique en todas las clases.
           Polimorfismo: Apesar de que nuestro metodo se llama igual en todas las clases no funciona de la misma manera.
Criterios_de_aceptacion: 
1. Registrar_informacion
2. Mostrar_informacion
3. Ejecutar_una_acción_propia _del_sistema
4. Dividir_en_categorias
5. Caracterizar_productos
6. Matener_segura_la_información_importante
