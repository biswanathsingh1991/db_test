
Vue.component('test12', {
  props: ['info'],
  data: function () {
    return {


    }
  },
    template: '#test12-template'
});



var allalbum = new Vue({

  el: '#allalbum',
  delimiters: ['[[', ']]'],
  data : {
    info: null,
    joy : "name-joy"
  },
    created (){
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
