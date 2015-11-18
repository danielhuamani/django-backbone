var publicacionesCollection = Backbone.Collection.extend({
	model: publicacionModel,
	url: '/api/noticias/',
	initialize: function(){
		console.log("Se creo una nueva collecion")
	}

});

var publicaciones = new publicacionesCollection();
publicaciones.fetch()
