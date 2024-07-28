document.addEventListener('alpine:init',()=>{
    localData=JSON.parse(localStorage.getItem('store'));
    Alpine.store('store',{
        open:  localData?localData.open:false,
        posts: localData?localData.posts:[],
        add(post){
            this.posts.push(post)
        },
        toggle(){
            this.open=!this.open
        },
    })
})