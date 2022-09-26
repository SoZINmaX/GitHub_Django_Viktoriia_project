<template>
    <div class="popup">
        <div class="popup-inner">
            <slot />
            <form id="commentForm" name="commentForm" novalidate="novalidate" @submit.prevent="handleSubmit">
                      <div class="row">
                          <div class="col-md-6">
                              <div class="form-group mb-3"><input class="form-control" type="text" id="name" placeholder="Your Name *" required v-model="post.name"><small class="form-text text-danger flex-grow-1 help-block lead"></small></div>
                              <div class="form-group mb-3"><input class="form-control" type="text" id="text" placeholder="Rate me *" required v-model="post.rate"><small class="form-text text-danger flex-grow-1 help-block lead"></small></div>
                          </div>
                          <div class="col-md-6">
                              <div class="form-group mb-3"><textarea class="form-control" id="message" placeholder="Your Comment *" required v-model="post.comment"></textarea><small class="form-text text-danger help-block lead"></small></div>
                          </div>
                          <div class="w-101"></div>
                          <div class="col-lg-12 text-center">
                              <div id="success"></div><button class="btn btn-primary btn-xl text-uppercase" id="sendMessageButton" type="submit">Send Message</button>
                          </div>
                      </div>
                  </form>
            <button class="btn btn-primary btn-xl text-uppercase" @click="TogglePopup">Close</button>
        </div>
    </div>
</template>

<script>

    import * as Vue from 'vue'
    import axios from 'axios'
    import VueAxios from 'vue-axios'

    const app = Vue.createApp()
    app.use(VueAxios, axios)

    export default {
        name: "Popup",

        props: ['TogglePopup'],

        data() {
          return {
              post:{
                name: null,
                comment: null,
                rate: null,
              },
          }
      },
      methods: {
        handleSubmit() {
          console.log(this.post)
          axios.post('api/v1/comment/list_add/', this.post).then((result)=>{console.log(result)})
        }
      },
    }
</script>

<style scoped>

.popup {
    position:fixed;
    top:0;
    left: 0;
    right: 0;
    bottom:0;
    z-index: 99;


    display: flex;
    align-items:center;
    justify-content: center;
}

.popup-inner {
    background-color: #fff;
    padding: 32px;
}


</style>