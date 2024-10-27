**Instructivo Detallado para Diseñar un Transformador de Columnas con Devanados Secundarios:**

**1. Requerimientos:**
   - Potencia nominal (`P`) en VA.
   - Tensiones primaria (`V1`) y secundaria (`V2`).
   - Frecuencia de operación (`f`) en Hz.
   - Número de devanados secundarios (`m`, si aplica).
   - Número de fases (`Nf`).

**2. Materiales:**
   - Núcleo: Láminas de acero al silicio.
   - Aislamiento: Material específico para devanados y conexiones.
   - Aceite: Dieléctrico y conforme a normativas.

**3. Cálculos Iniciales:**
   - Corriente primaria (`I1`): 
      $$ I1 = \frac{P}{\sqrt{3} \cdot V1} $$

   - Corriente secundaria (`I2`): 
      $$ I2 = \frac{I1}{N} $$

   - Corriente en devanado secundario (`I2m`):
      $$ I2m = \frac{I1}{N \cdot m} $$

**4. Diseño del Núcleo:**
   - Sección transversal (`A`):
      $$ A = \frac{P}{4.44 \cdot Nf \cdot f \cdot B_{max}} $$

**5. Número de Espiras:**
   - Espiras en el primario (`N1`):
      $$ N1 = \frac{V1}{4.44 \cdot Nf \cdot f \cdot B_{max} \cdot A} $$

   - Espiras en el secundario (`N2`):
      $$ N2 = N1 \cdot N $$

   - Espiras en devanado secundario (`N2m`):
      $$ N2m = N2 \cdot m $$

**6. Diseño de Devanados:**
   - Calibre del alambre para devanados primario y secundario.
   - Asegurar espacio suficiente en el núcleo para todos los devanados y conexiones.

**7. Selección del Aceite:**
   - Elija aceite dieléctrico conforme a normativas.

**8. Verificación de Pérdidas y Eficiencia:**
   - Pérdidas en el cobre (`Pc`) y en el núcleo (`Pn`).
   - Eficiencia (n):
      $$ \eta = \frac{P}{P + Pc + Pn} $$

**Consideraciones Modificables:**
   - Ajusta las fórmulas según el número de fases (`Nf`).
   - Modifica las fórmulas de corriente y número de espiras según la cantidad de devanados secundarios (`m`).

**Referencias:**
   1. "Transformers and Inductors for Power Electronics" - W.G. Hurley y W.H. Wolfle.
   2. "Transformer Engineering: Design, Technology, and Diagnostics" - S.V. Kulkarni y S.A. Khaparde.
   3. "Power Transformer Handbook" - John Winders.

Recuerda adherir a normativas de seguridad eléctrica y rendimiento. Personaliza las fórmulas según las necesidades específicas de tu diseño.
