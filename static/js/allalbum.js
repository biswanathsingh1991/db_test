
Vue.component('test12', {
  props: ['title'],
  data: function () {
    return {
      

    }
  },
    template: '<div> <ul><li v-for="title in title">{{ title.title }}<li></ul></div>'
});



var allalbum = new Vue({

  el: '#allalbum',
  delimiters: ['[[', ']]'],
  data : {
    info: null,
    joy : "name-joy"
  },
    mounted (){
      // $.ajax({
      //   url : '/allalbumapi/',
      //   dataType : 'json',
      //   type : 'GET',
      //   success : function(data){
      //     this.obj = data;
      //     // this.obj.valueset = true ;
      //   }
      //
      // })

      axios
     .get('/allalbumapi/')
     .then(response => (this.info = response))
  },

});
