[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ZtQ31pSG)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19828959)
# 🔐 PWASP SCANNER – Sistema de Detección de Vulnerabilidades Web

**Ubicación:** Tacna, Perú  
**Año:** 2025  
**Autor:** Joel Robert Ccalli Chata

---

## 📌 Descripción General del Proyecto

El **PWASP SCANNER** es un sistema web diseñado para detectar **vulnerabilidades en aplicaciones web** basándose en los estándares del **OWASP Top 10**, facilitando el análisis de seguridad en sitios de pequeñas y medianas empresas. El sistema permite escanear sitios ingresando una URL, autenticarse si es necesario, identificar vulnerabilidades como XSS, SQLi, CSRF, etc., y generar reportes técnicos detallados en múltiples formatos.

> Este proyecto nace de la necesidad creciente de automatizar procesos de evaluación de seguridad, sin depender de costosas auditorías manuales o herramientas complejas.

---

## 🧱 Estructura del Proyecto

El sistema se desarrolló bajo una metodología ágil (SCRUM) y se documentó en seis entregables clave:

---

## 📄 Documentación Técnica

| Documento | Descripción | Enlace |
|----------|-------------|--------|
| **FD01 - Ficha del Proyecto** | Contiene los datos generales del proyecto: nombre, responsable, ubicación, objetivos generales, tiempo estimado, etc. | [Ver FD01](#) |
| **FD02 - Documento de Visión** | Presenta una descripción extensa del sistema, su valor para los usuarios, actores involucrados, contexto de uso, y funcionalidades clave esperadas. | [Ver FD02](#) |
| **FD03 - Especificación de Requisitos de Software (SRS)** | Documento detallado de requisitos funcionales y no funcionales, casos de uso (con PlantUML), y diagramas de secuencia (Mermaid). | [Ver FD03](#) |
| **FD04 - Diseño de Arquitectura del Software (SAD)** | Contiene el diagrama de arquitectura general, tecnologías empleadas, capas del sistema, módulos internos y su interacción. | [Ver FD04](#) |
| **FD05 - Informe Final del Proyecto** | Informe técnico con justificación, desarrollo, evidencias, pruebas realizadas, resultados obtenidos, y conclusiones. | [Ver FD05](#) |
| **FD06 - Propuesta de Proyecto** | Propuesta detallada del sistema: introducción, objetivos, justificación, cronograma, presupuesto, metodología y referencias bibliográficas. | [Ver FD06](#) |

---

## 🔍 Tecnologías Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript (Vanilla o React opcional)
- **Backend:** Python (Flask), con librerías para escaneo (requests, BeautifulSoup, OWASP ZAP API)
- **Base de datos:** SQLite / PostgreSQL (según necesidad)
- **Herramientas de Seguridad:** OWASP ZAP, Nmap, Sqlmap
- **Despliegue:** Hosting compartido o VPS (como Somee.com, Heroku, etc.)

---

## 🧠 Funcionalidades Principales

- ✅ Escaneo de sitios web por URL
- ✅ Detección de vulnerabilidades OWASP Top 10
- ✅ Panel de usuario para historial de escaneos
- ✅ Reportes exportables (PDF, CSV)
- ✅ Modo de escaneo autenticado (Login)
- ✅ Interfaz amigable y adaptable (responsive)

---

## 🖥️ Diagrama General del Sistema

![Diagrama Arquitectura General](./assets/diagrama-arquitectura-pwasp.png)

> *Incluye capas: presentación, lógica de negocio, motor de escaneo, base de datos y generación de reportes.*

---

## 📆 Cronograma de Desarrollo

| Fase | Actividades | Mes |
|------|-------------|-----|
| Análisis | Recolección de requerimientos, OWASP Top 10 | Julio |
| Diseño | Arquitectura, casos de uso, diagramas | Julio |
| Desarrollo | Backend, frontend, motor de escaneo | Agosto - Septiembre |
| Pruebas | Validación, reportes, pruebas automatizadas | Septiembre |
| Despliegue | Entrega final, documentación, evaluación | Octubre |

---

## 💼 Autor

- 👤 **Joel Robert Ccalli Chata**
- 📍 Tacna, Perú
- 📧 joelccalli@example.com

---

## 📚 Referencias Bibliográficas

1. OWASP Foundation. (2023). *OWASP Top 10: Web Application Security Risks*. https://owasp.org
2. Stallings, W. (2020). *Cryptography and Network Security*. Pearson.
3. Grimes, R. (2021). *Hacking the Hacker*. Wiley.
4. Kim & Solomon. (2020). *Fundamentals of Information Systems Security*. Jones & Bartlett.
5. Anderson, R. (2020). *Security Engineering*. Wiley.
6. Allen, J. (2022). *Software Security Engineering*. Addison-Wesley.
7. Bishop, M. (2018). *Computer Security: Art and Science*. Addison-Wesley.
8. Zetter, K. (2015). *Countdown to Zero Day*. Crown Publishing.
9. OWASP ZAP. (2023). *Zed Attack Proxy*. https://owasp.org/www-project-zap/
10. ISO/IEC 27001:2022. *Information Security Management Systems*. ISO.

---

## 📦 Estado del Proyecto

```bash
🚧 EN DESARROLLO – Fase de validación y pruebas finales
