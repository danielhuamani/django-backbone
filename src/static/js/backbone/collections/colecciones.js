var publicacionesCollection = Backbone.Collection.extend({
	model: publicacionModel,
	url: '/api/noticias/',
	ordenar: 'id',
	initialize: function(){
		console.log("Se creo una nueva collecion")
	},
	comparator: function(item){
		return -item.get(this.ordenar)
	},
	filtrarpalabra: function(palabra){
		filter = this.filter(function(modelo) {
			return modelo.get('descripcion').indexOf(palabra) != -1;
		});
		return filter;
	}

});

var publicaciones = new publicacionesCollection();
publicaciones.fetch()


$("#buscar_publicaciones").keyup(function(event) {
	/* Act on the event */
	console.log(publicaciones.filtrarpalabra($(this).val()))
});