<template>
    <div class="popup">
        <div class="popup-inner">
            <slot />
            <h4 v-if="this.status_code != 201 && !this.response_errors">Leave your comment</h4>
            <form id="commentForm" name="commentForm" novalidate="novalidate" @submit.prevent="handleSubmit">
                <div class="row-cols">
                    <h4 v-if="this.response_errors">Sorry, something went wrong.<p>Please correct Your input and try again.</p></h4>
                    <div class="col-md" v-if="this.status_code != 201">
                        <div class="form-group mb-3"><input class="form-control" type="text" id="name" placeholder="Your Name *" required v-model="post.name"><small class="form-text text-danger flex-grow-1 help-block lead"></small></div>
                        <div class="form-group mb-3"><select class="form-control" type="text" id="text" required v-model="post.rate">
                        <option value="5">Very Satisfied</option>
                        <option value="4">Satisfied</option>
                        <option value="3">Good</option>
                        <option value="2">Dissatisfied</option>
                        <option value="1" selected>Very Dissatisfied</option>
                        </select><small class="form-text text-danger flex-grow-1 help-block lead"></small></div>
                        <div class="form-group mb-3"><textarea class="form-control" id="message" placeholder="Your Comment *" required v-model="post.comment"></textarea><small class="form-text text-danger help-block lead"></small></div>
                    </div>
                          <div class="row-cols">
                                <h4 v-if="this.status_code === 201">Comment was sucessfully added.<p>Thank You for Your time.</p></h4>
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
                rate: '5',
              },
              errors: [],
              status_code: '',
              response_errors: '',
          }
      },
      methods: {
        handleSubmit() {
        this.status_code = ''
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
    background-color:rgba(0, 0, 0, 0.5);


    display: flex;
    align-items:center;
    justify-content: center;
}

.popup-inner {
    background-color: #fff;
    border-radius: 15px;
    padding: 32px;
}


</style>