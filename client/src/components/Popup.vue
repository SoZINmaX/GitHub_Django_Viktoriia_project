<template>
    <div class="popup">
        <div class="popup-inner">
            <slot />
            <h2 v-if="this.status_code != 201">Leave your comment</h2>
            <form id="commentForm" name="commentForm" novalidate="novalidate" @submit.prevent="handleSubmit">
                <div class="row-cols">
                    <div class="col-md" v-if="this.status_code != 201">
                        <div class="form-group mb-3"><input class="form-control" type="text" id="name" placeholder="Your Name *" required v-model="post.name"><small class="form-text text-danger flex-grow-1 help-block lead"></small></div>
                        <div class="form-group mb-3"><input class="form-control" type="text" id="text" placeholder="Rate me *" required v-model="post.rate"><small class="form-text text-danger flex-grow-1 help-block lead"></small></div>
                        <div class="form-group mb-3"><textarea class="form-control" id="message" placeholder="Your Comment *" required v-model="post.comment"></textarea><small class="form-text text-danger help-block lead"></small></div>
                    </div>
                          <div class="row-cols">
                                <h2 v-if="this.status_code === 201">Message was succesfully sent.<p>I will get in touch with You soon.</p></h2>
                                <h2 v-if="this.response_errors">Sorry, something went wrong.<p>Please correct Your input and try again.</p></h2>
                                <p v-if="errors.length">
                                    <b>Please correct the following error(s):</b>
                                    <ul>
                                    <li v-for="error in errors">{{ error }}</li>
                                    </ul>
                                </p>
                          </div>
                          <div class="button_box">
                            <div class="w-101"></div>
                                <div class="row">
                                    <div class="form-group mb-3">
                                        <button class="btn btn-primary btn-xl text-uppercase" id="sendMessageButton" type="submit" v-if="this.status_code != 201">Send Message</button>
                                    </div>
                                    <div class="form-group mb-3">
                                        <button class="btn btn-primary btn-xl text-uppercase" @click="TogglePopup">Close</button>
                                    </div>
                                </div>
                          </div>
                      </div>
                  </form>
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
              errors: [],
              status_code: '',
              response_errors: '',
          }
      },
      methods: {
        handleSubmit() {
        this.response_errors = ''
        if (this.post.name && this.post.comment && this.post.rate) {
        axios.post('api/v1/comment/list_add/', this.post).then(response => (this.status_code = response.status)).catch(error => (this.response_errors = error));
        }

        this.errors = [];

        if (!this.post.name) {
        this.errors.push('Name required.');
        }

        if (!this.post.comment) {
        this.errors.push('Comment required.');
        };
      
        if (!this.post.rate) {
        this.errors.push('Rating required.');
        };
      
        },
    }
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