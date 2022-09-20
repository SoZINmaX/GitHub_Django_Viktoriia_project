<template>
    <div>
        <ul>
            <li v-for="comment in comments">{{ comment }}</li> 
        </ul>
    </div>
</template>
<script>
    export default {
        name: "Home",
        data() {
            return {
                comments: []
            }
        },
    async beforeMount () {
        let response = await fetch('api/v1/comment/list_add/')
        console.log(response)
        if (response.status_code === 200){
            this.comments = await response.json()
        }
    }
}
</script>
<style scoped>
    p {
    font-size: 2.5em;
    text-align: center;
    }
</style>