// vue component
Vue.component('tracks',{
  props: ['tracks_info'],
  data: function(){
    return{
      
    }

  },
  template: '#tracks-template'

});




// ############################################
// vue element
var tracks = new Vue({
  el: '#tracks',
  delimiters: ['[[', ']]'],
  data: {
    tracks_info: null,

  },
  created(){
    axios
   .get('/alltracksapi/')
   .then(response => (this.tracks_info = response))
},
});
