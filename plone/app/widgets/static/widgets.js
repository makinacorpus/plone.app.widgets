!function(a){"use strict";a(document).ready(function(){var b=document.createElement("script");b.setAttribute("type","text/javascript"),b.setAttribute("src","/++resource++mockup/js/config.js"),b.onload=function(){requirejs.config({baseUrl:"++resource++mockup/"}),0===a('[data-iframe="plone-toolbar"]').size()?require(["mockup-bundles-widgets"]):require(["mockup-bundles-widgets","mockup-iframe_init"])};var c=document.createElement("script");c.setAttribute("type","text/javascript"),c.setAttribute("src","/++resource++mockup/bower_components/requirejs/require.js"),c.onload=function(){document.getElementsByTagName("head")[0].appendChild(b)},document.getElementsByTagName("head")[0].appendChild(c);var d=document.createElement("style");if(d.setAttribute("type","text/less"),d.innerHTML="@import (less) \"/++resource++mockup/less/widgets.less\"; @isBrowser: true; @pathPrefix: '/++resource++mockup/less/';",document.getElementsByTagName("head")[0].appendChild(d),0!==a('[data-iframe="plone-toolbar"]').size()){var e=document.createElement("style");e.setAttribute("type","text/less"),e.innerHTML="@import (less) \"/++resource++mockup/less/iframe_init.less\"; @isBrowser: true; @pathPrefix: '/++resource++mockup/less/';",document.getElementsByTagName("head")[0].appendChild(e)}var f=document.createElement("script");f.setAttribute("type","text/javascript"),f.setAttribute("src","/++resource++mockup/node_modules/grunt-contrib-less/node_modules/less/dist/less-1.4.1.js"),document.getElementsByTagName("head")[0].appendChild(f)})}(jQuery);