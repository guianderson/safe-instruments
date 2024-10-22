var app = new Vue({
    delimiters: ["[[", "]]"],
    el: '#app',
    data: {
        clicked: false,
    },
    methods:{
        userClicked: function() {
             this.clicked = !this.clicked
             this.$refs.form.submit()
             },
            }
    });
