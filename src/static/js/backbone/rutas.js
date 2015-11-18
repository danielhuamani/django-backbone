var rutas = Backbone.Router.extend({
	routes: {
		'publicaciones': 'publicaciones',
		'publicaciones/:id': 'detalle',
	},
	detalle: function(id){
		console.log(id)
	},
	publicaciones: function(){
		console.log("home");
	}
});

var route = new rutas();
Backbone.history.start()
Backbone.history.navigate('publicaciones')
