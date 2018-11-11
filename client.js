// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Send back to the popup a sorted deduped list of valid link URLs on this page.
// The popup injects this script into all frames in the active tab.
if(document.location != "https://portalcfdi.facturaelectronica.sat.gob.mx/ConsultaEmisor.aspx" && document.location != "https://portalcfdi.facturaelectronica.sat.gob.mx/ConsultaReceptor.aspx"){
  if(new RegExp("https://portalcfdi.facturaelectronica.sat.gob.mx/*").test(document.location)){
    alert("Vaya a la seccion de consulta de facturas Emitidas/Recibidas para descargar");
  }else{
    if(confirm("No se encuentra en la pagina de Facturacion del SAT. ¿Desea que lo llevemos al sitio?")){
      window.open('https://portalcfdi.facturaelectronica.sat.gob.mx', '_blank');
    }
  }
}else{
  var links = document.getElementsByName("BtnDescarga");
  
  alert("Se van a descargar " + links.length + " CFDI's");
  for (var i = 0; i < links.length; i++) {
    window.open('https://portalcfdi.facturaelectronica.sat.gob.mx/' + links[i].getAttribute('onclick').substr(19).slice(0,-18));
  }
}