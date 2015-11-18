var publicacionModel = Backbone.Model.extend({
	urlRoot: '/api/noticias/',
	resumen: "Api para publicaciones",
	defaults:{
		titulo: "titulo para publicacion",
		descripcion: "descripcion",
		fecha: "fecha creacio",
		tipo: "pk tipo de noticia"
	}

});
