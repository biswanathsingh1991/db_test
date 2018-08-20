
Vue.component('test12', {
  props: ['title'],
  data: function () {
    return {
      count:0,

    }
  },
    template: '<div> <ul><li v-for="title in title">{{ title.title }}<li></ul></div>'
}),



var allalbum = new Vue({

  el: '#allalbum',
  delimiters: ['[[', ']]'],
  data:{
  },
  mounted (){
    $ajax({
      url : '/allalbumapi/',
      dataType: "json",
      type: "GET",
      sucess: function(data){
        console.log(data)
        this.obj = data
      },
    }),
  } ,

})
