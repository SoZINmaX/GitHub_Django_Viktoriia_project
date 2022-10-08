<template>
  <body id="page-top" data-bs-spy="scroll" data-bs-target="#mainNav" data-bs-offset="54">
  <header class="masthead" >
      <div class="container">
        <div class="select_language">
              <select v-model="locale">
                <option value="en">Русский</option>
                <option value="ua">Українська</option>
                <option value="ru">English</option>
              </select>
              <span>{{ t('choose language') }}</span>
          </div>
          <div class="intro-text">
              <div class="intro-lead-in"><span>{{ t('Welcome') }}</span></div>
              <div class="intro-heading text-uppercase"><span>{{ t('It is Nice To See You Here') }}</span></div><a class="btn btn-primary btn-xl text-uppercase" role="button" href="#about">{{ t('more about myself') }}</a>
          </div>
      </div>
  </header>
  <!-- ======= About Section ======= -->
  <section id="about" class="about">
      <div class="container">

        <div class="block-heading">
          <h1>{{ t('About') }}</h1>
        </div>

        <div class="row">
          <div class="col-lg-4" data-aos="fade-right">
            <img src="src/assets/assets/img/photo.png" class="img-fluid" alt="">
          </div>
          <div class="col-lg-8 pt-4 pt-lg-0 content" data-aos="fade-left">

            <p class="fst-italic">
              
            </p>
            <p>
              <p><h4>{{ t('Lets get acquainted') }}</h4></p>
              <p>{{ t('Psychology i like') }}</p>
              <p>{{ t('I was economy') }}</p>
              <ul>
                <p><h5>{{ t('education') }}</h5></p>
                <li><i class="bi bi-chevron-right"></i> <strong>⭐️</strong> <span>{{ t('self') }}</span></li>
                <li><i class="bi bi-chevron-right"></i> <strong>⭐️</strong> <span>{{ t('relations') }}</span></li>
                <li><i class="bi bi-chevron-right"></i> <strong>⭐️</strong> <span>{{ t('consult') }}</span></li>
              </ul>
              <p>{{ t('new way') }}</p>
            </p>
          </div>
        </div>

      </div>
  </section>
  <!-- End About Section -->
  <!-- ======= Diploma Section ======= -->
  <section id="portfolio" class="clean-block slider dark" style="margin-bottom: -1px;">
      <div class="container">
          <div class="block-heading">
            <h1>{{ t('diplomas') }}</h1>
          </div>
          <div class="carousel slide" data-bs-ride="carousel" id="carousel-1">
              <div class="carousel-inner">
                  <div class="carousel-item active"><img class="w-100 d-block" src="src/assets/assets/img/scenery/image1.jpeg" alt="Slide Image"></div>
                  <div class="carousel-item"><img class="w-100 d-block" src="src/assets/assets/img/scenery/image2.jpeg" alt="Slide Image"></div>
                  <div class="carousel-item"><img class="w-100 d-block" src="src/assets/assets/img/scenery/image3.jpeg" alt="Slide Image"></div>
              </div>
              <div><a class="carousel-control-prev" href="#carousel-1" role="button" data-bs-slide="prev"><span class="carousel-control-prev-icon"></span><span class="visually-hidden">Previous</span></a><a class="carousel-control-next" href="#carousel-1" role="button" data-bs-slide="next"><span class="carousel-control-next-icon"></span><span class="visually-hidden">Next</span></a></div>
              <ol class="carousel-indicators">
                  <li data-bs-target="#carousel-1" data-bs-slide-to="0" class="active"></li>
                  <li data-bs-target="#carousel-1" data-bs-slide-to="1"></li>
                  <li data-bs-target="#carousel-1" data-bs-slide-to="2"></li>
              </ol>
          </div>
      </div>
  </section>
  <!-- End of Diploma Section -->
  <!-- ======= Comments Section ======= -->
  <section id="review">
    <div class="container">
          <div class="block-heading">
            <h1>{{ t('comments') }}</h1>
          </div>
          <div class="carousel slide" data-bs-ride="carousel" id="carousel-2">
              <div class="carousel-inner">
                  <div class="carousel-item active">
                    <div class="d-flex media">
                        <div class="comment-box">
                          <tr v-for="comment in comments1" :key="comment.comment">
                            <td>
                              <h4>{{ comment.name }}</h4>
                              <div>
                                  <p v-if="comment.rate == 1">⭐️</p>
                                  <p v-if="comment.rate == 2">⭐️⭐️</p>
                                  <p v-if="comment.rate == 3">⭐️⭐️⭐️</p>
                                  <p v-if="comment.rate == 4">⭐️⭐️⭐️⭐️</p>
                                  <p v-if="comment.rate == 5">⭐️⭐️⭐️⭐️⭐️</p>
                              </div>
                              <p>{{ comment.comment }}</p>
                              <p><span class="reviewer-name"></span><span class="review-date">{{ comment.date }}</span></p>
                            </td>
                          </tr>
                        </div>
                    </div>
                 </div>
                 <div v-if="comments2" class="carousel-item">
                    <div class="comment-box">
                        <div class="media-body">
                          <tr v-for="comment in comments2" :key="comment.comment">
                            <td>
                              <h4>{{ comment.name }}</h4>
                              <div>
                                  <p v-if="comment.rate == 1">⭐️</p>
                                  <p v-if="comment.rate == 2">⭐️⭐️</p>
                                  <p v-if="comment.rate == 3">⭐️⭐️⭐️</p>
                                  <p v-if="comment.rate == 4">⭐️⭐️⭐️⭐️</p>
                                  <p v-if="comment.rate == 5">⭐️⭐️⭐️⭐️⭐️</p>
                              </div>
                              <p>{{ comment.comment }}</p>
                              <p><span class="reviewer-name"></span><span class="review-date">{{ comment.date }}</span></p>
                            </td>
                          </tr>
                        </div>
                    </div>
                 </div>
                <div v-if="comments3" class="carousel-item" >
                    <div class="comment-box">
                        <div class="media-body">
                          <tr v-for="comment in comments3" :key="comment.comment">
                            <td>
                              <h4>{{ comment.name }}</h4>
                              <div>
                                  <p v-if="comment.rate == 1">⭐️</p>
                                  <p v-if="comment.rate == 2">⭐️⭐️</p>
                                  <p v-if="comment.rate == 3">⭐️⭐️⭐️</p>
                                  <p v-if="comment.rate == 4">⭐️⭐️⭐️⭐️</p>
                                  <p v-if="comment.rate == 5">⭐️⭐️⭐️⭐️⭐️</p>
                              </div>
                              <p>{{ comment.comment }}</p>
                              <p><span class="reviewer-name"></span><span class="review-date">{{ comment.date }}</span></p>
                            </td>
                          </tr>
                        </div>
                    </div>
                </div>
              </div>
              <div><a class="carousel-control-prev" href="#carousel-2" role="button" data-bs-slide="prev"><span class="carousel-control-prev-icon"></span><span class="visually-hidden">Previous</span></a><a class="carousel-control-next" href="#carousel-2" role="button" data-bs-slide="next"><span class="carousel-control-next-icon"></span><span class="visually-hidden">Next</span></a></div>
              <ol class="carousel-indicators">
                  <li data-bs-target="#carousel-2" data-bs-slide-to="0" class="active"></li>
                  <li data-bs-target="#carousel-2" data-bs-slide-to="1"></li>
                  <li data-bs-target="#carousel-2" data-bs-slide-to="2"></li>
              </ol>
          </div>
          <div class="col-lg-12 text-center">
              <div id="success"></div><button class="btn btn-primary btn-xl text-uppercase" id="sendCommentButton" @click="() => TogglePopup('buttonTrigger')">{{ t('leave comment') }}</button>
              <component v-if="popupTriggers.buttonTrigger" :TogglePopup="() => TogglePopup('buttonTrigger')" :is="Popup">
              </component>
          </div>
      </div>
  </section>
  <!-- End of Comments Section -->
  <!-- ======= Contact Section ======= -->
  <section class="py-5"></section>
  <section id="contact">
      <div class="container">
          <div class="row">
              <div class="col-lg-12 text-center">
                  <h2 class="text-uppercase section-heading">{{ t('call me') }}</h2>
                  <h3 class="text-muted section-subheading">{{ t('i will call u') }}</h3>
              </div>
          </div>
          <div class="row">
              <div class="col-lg-12">
                  <form id="contactForm" name="contactForm" novalidate="novalidate" @submit.prevent="handleSubmit">
                      <div class="row">
                          <div class="col-md-6">
                              <div class="form-group mb-3"><input class="form-control" type="text" id="name" placeholder="Your Name *" required v-model="posts.name"><small class="form-text text-danger flex-grow-1 help-block lead"></small></div>
                              <div class="form-group mb-3"><input class="form-control" type="email" id="email" placeholder="Your Email *" required v-model="posts.email"><small class="form-text text-danger help-block lead"></small></div>
                              <MazPhoneNumberInput
                              v-model="phoneNumber"
                              show-code-on-list
                              color="info"
                              :preferred-countries="['UA', 'PL', 'FR', 'BE', 'DE', 'US', 'GB']"
                              :ignored-countries="['AC']"
                              @update="posts.results = $event"
                              :success="posts.results?.isValid"
                            />
                          </div>
                          <div class="col-md-6">
                              <div class="form-group sm-1"><textarea class="form-control" id="message" placeholder="Your Message *" required v-model="posts.message"></textarea><small class="form-text text-danger help-block lead"></small></div>
                          </div>
                          <div class="w-101"></div>
                          <div class="col-lg-12 text-center">
                              <div id="success"></div><button class="btn btn-primary btn-xl text-uppercase" id="sendMessageButton" type="submit" @click="() => TogglePopupClient('buttonTrigger')">{{ t('write') }}</button>
                              <component v-if="popupTriggersClient.buttonTrigger" :TogglePopupClient="() => TogglePopupClient('buttonTrigger')" :is="Popupclient">
                                <h4 v-if="this.status_code === 201">{{ t('success') }}<p>{{ t('i will call u i the nearest') }}</p></h4>
                                <h4 v-if="this.response_errors">{{ t('sorry') }}<p>{{ t('please fill up') }}</p></h4>
                                <p v-if="errors.length">
                                  <b>{{ t('please fill up all') }}</b>
                                  <ul>
                                    <li v-for="error in errors">{{ error }}</li>
                                  </ul>
                                </p>
                              </component>
                          </div>
                      </div>
                  </form>
              </div>
          </div>
      </div>
  </section>
  <!-- End of Contact Section -->
  <footer>
      <div class="container">
          <div class="row">
              <div class="col-md-12">
                  <ul class="list-inline social-buttons">
                      <li class="list-inline-item"><a href="https://www.tiktok.com/@belinskaya_victoriya?is_from_webapp=1&sender_device=pc"><i class="fab fa-tiktok fa-1x"></i></a></li>
                      <li class="list-inline-item"><a href="https://www.youtube.com/channel/UCCfbZnRGt6kE58DULc3BNUA"><i class="fab fa-youtube fa-1x"></i></a></li>
                      <li class="list-inline-item"><a href="https://www.instagram.com/belinskaya_victoriya/"><i class="fab fa-instagram"></i></a></li>
                  </ul>
              </div>
          </div>
      </div>
  </footer>
</body>
</template>
<script >

import { ref } from 'vue'
import Popup from './components/Popup.vue';
import Popupclient from './components/Popupclient.vue';
import * as Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import MazPhoneNumberInput from "maz-ui/components/MazPhoneNumberInput";
import { useI18n } from 'vue-i18n'


const app = Vue.createApp()
app.use(VueAxios, axios)

export default {
      name: "home",
      
      components: { MazPhoneNumberInput },

      setup() {
        const popupTriggers = ref({
          buttonTrigger:false,
        });
        const popupTriggersClient = ref({
          buttonTrigger:false,
        });

        const TogglePopup = (trigger) => {
          popupTriggers.value[trigger] = !popupTriggers.value[trigger]
        };
        const TogglePopupClient = (trigger) => {
          popupTriggersClient.value[trigger] = !popupTriggersClient.value[trigger]
        };
        const { t, locale } = useI18n({
          useScope: 'global',
        })
        return {
            Popup,
            Popupclient,
            popupTriggers,
            TogglePopup,
            popupTriggersClient,
            TogglePopupClient,
            t,
            locale,
          }
      },

      data() {
          return {
              posts:{
                name: null,
                email: null,
                message: null,
                results:'',
              },
              number: '',
              comments: [],
              errors: [],
              status_code: '',
              response_errors: '',
              phoneNumber:'',
          }
      },

      computed: {
        comments1() {
          var keyCount = Object.keys(this.comments).length
          if (keyCount < 1){
            return null

          } else {
            return this.comments.slice(0, 2)
          }
        },
        comments2() {
          var keyCount = Object.keys(this.comments).length
          if (keyCount < 3){
            return null

          } else {
            return this.comments.slice(2, 4)
          }
        },
        comments3() {
          var keyCount = Object.keys(this.comments).length
          if (keyCount < 5){
            return null

          } else {
            return this.comments.slice(4, 6)
          }
        }
      },

      methods: {
      handleSubmit() {

      this.response_errors = ''
      this.status_code= ''

      if (this.posts.name && this.posts.results.isValid === true && this.posts.email && this.posts.message && this.validEmail(this.posts.email)) {
        axios.post('api/v1/client/add/', {name: this.posts.name , email: this.posts.email, message: this.posts.message, phone_number: this.posts.results.e164}).then(response => (this.status_code = response.status)).catch(error => (this.response_errors = error));
      }

      this.errors = [];

      if (!this.posts.name) {
        this.errors.push('Name required.');
      }
      if (!this.posts.results.isValid === true) {
        this.errors.push('Phone number required.');
      }
      if (!this.posts.email) {
        this.errors.push('Email required.');
      } 
      else if (!this.validEmail(this.posts.email)) {
        this.errors.push('Valid email required.');
      }
      if (!this.posts.message) {
        this.errors.push('Message required.');
      }
    },
      validEmail: function (email) {
      var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
  },
      async beforeMount () {
      const response = await fetch('api/v1/comment/list_add/')
      if (response.status === 200){
      this.comments = await response.json()
    }
  }
}
</script>

<i18n global="ru">
  {
    "ru": {
      "Welcome": "Welcome to my psychology website!",
      "choose language": "Choose a language",
      "It is Nice To See You Here": "It's nice to see you here)",
      "more about myself":"Learn more",
      "About":"Information About Me",
      "Lets get acquainted":"Let's get acquainted with how I became a psychologist and why?",
      "Psychology i like": "Psychology has always been interesting to me, listening to, helping a person was very valuable and important for me. I was always interested to know why we behave this way, where this or that belief originates. Even at the university, when we had psychology in the first year - I prepared reports with special trepidation and interest.",
      "I was economy": "I am an economist and worked in this area for a long time, but I realized that helping colleagues to find about themselves, resolve a conflict, find an approach to any person or just listen to them is much more interesting, so I decided to turn my life around 180 ° and start over.",
      "education":"So my education is:",
      "self":"Psychology of personality.",
      "relations":"Psychology of relationships.",
      "consult":"Now I'm a certified consulting psychologist.",
      "new way":"I practice a client-centered approach, and also combine different techniques for a more effective result.
              A client-centered approach means following the client, since all the answers are always in ourselves, sometimes we just need help to find them.",
      "diplomas":"My diplomas",
      "comments":"Reviews and comments",
      "leave comment":"Leave a comment",
      "call me": "Contact me",
      "i will call u": "I will call You when and how it is comfortable for You",
      "write":"Sign up for a consultation",
      "success":"Message sent successfully",
      "i will call u i the nearest": "I will contact You shortly.",
      "sorry":"Sorry, something went wrong.",
      "please fill up": "Please fill in all fields correctly and try again.",
      "please fill up all":"Please fill in all fields:",
      "close":"Close",
      "5":"Very Satisfied",
      "4":"Satisfied",
      "3":"Good",
      "2":"Dissatisfied",
      "1":"Very Dissatisfied",
      "comment ok":"Comment sucessfully added, thanks.",
      "comment ok reload":"Reload this page to check it out.",

    },
    "ua": {
      "Welcome": "Ласкаво прошу на мій сайт із психології!",
      "choose language": "Оберіть мову",
      "It is Nice To See You Here":"Рада тебе тут бачити)",
      "more about myself":"Дізнатися більше",
      "About":"Інформація Про Мене",
      "Lets get acquainted":"Давайте знайомитись: як і чому я стала психологом?",
      "Psychology i like":"Психологія мені була цікава завжди, вислухати, допомогти людині було для мене дуже цінно і важливо. Мені з дитинства було цікаво знати відповідь на питання: «чому ми так себе поводимо, де бере початок те чи інше переконання?». Навіть в університеті, коли в нас була психологія на першому курсі - я готувала доповіді з особливим натхненням та завзятістю.",
      "I was economy":"Я - економіст і довго працювала в цій сфері, але зрозуміла: що допомагати колегам знайти себе, вирішити конфлікт, знайти підхід до будь-якої людини, або просто вислухати, мені набагато цікавіше; тому я вирішила змінити своє життя на 180° і почати з початку.",
      "education":"Отже, моя освіта:",
      "self":"Курс «Практична психологія».",
      "relations":"Курс «Психологія відносин».",
      "consult":"А тепер я дипломований психолог-консультант.",
      "new way": "Я практикую клієнт-центрований підхід, а також поєдную різні методики для більш ефективного результату.
              Клієнт-центрований підхід має на увазі слідування за клієнтом, тому що всі відповіді завжди є в нас самих, і іноді нам просто потрібна допомога, щоб їх знайти.",
      "diplomas":"Мої Дипломи",
      "comments":"Відгуки та коментарі",
      "leave comment":"Залиште коментар",
      "call me":"Зв'язатися зі мною",
      "i will call u":"Я зв'яжуся з Вами, коли і як Вам буде зручно",
      "write":"Записатися на консультацію",
      "success":"Повідомлення успішно надіслано",
      "i will call u i the nearest":"Я зв'яжуся з Вами найближчим часом.",
      "sorry":"Вибачте, щось пішло не так.",
      "please fill up":"Будь ласка, заповніть всі поля правильно і спробуйте ще раз.",
      "please fill up all":"Будь ласка заповніть усі поля:",
      "close":"Закрити",
      "5":"Дуже добре",
      "4":"Добре",
      "3":"Задовільно",
      "2":"Незадовільно",
      "1":"Погано",
      "comment ok":"Відгук успішно додано, дякую.",
      "comment ok reload":"Перезавантажте сторінку щоб його побачити.",
    },
    "en": {
      "Welcome": "Добро пожаловать на мой сайт по психологии!",
      "choose language": "Выберите язык",
      "It is Nice To See You Here":"Рада тебя здесь видеть)",
      "more about myself":"Узнать больше",
      "About":"Информация Обо Мне",
      "Lets get acquainted":"Давайте знакомится: как и почему я стала психологом?",
      "Psychology i like":"Психология мне была интересна всегда,выслушать, помочь человеку было для меня очень ценно и важно. Мне с детства было интересно знать ответ на вопрос:«почему мы так себя ведём, где берет начало то или иное убеждение?». Даже в университете, когда у нас была психология на первом курсе, я готовила доклады с особым трепетом и интересом.",
      "I was economy":"По первому образованию я экономист и долго работала в этой сфере, но я поняла, что помогать коллегам разобраться в себе, решить конфликт, найти подход к любому человеку или просто выслушать - мне намного интереснее, поэтому я решила развернуть свою жизнь на 180* и начать с начала.",
      "education":"Итак, мое образование:",
      "self":"Курс «Практическая психология»;",
      "relations":"Курс «Психология отношений»;",
      "consult":"А теперь я дипломированный психолог-консультант.",
      "new way":"Я практикую клиент-центрированный подход,а также совмещаю разные методики для более эффективного результата .
              Клиент -центрированный подход подразумевает под собой следование за клиентом, так как все ответы всегда есть в нас самих,иногда нам просто нужна помощь ,что бы их найти.",
      "diplomas":"Мои Дипломы",
      "comments":"Отзывы и комментарии",
      "leave comment":"Оставьте комментарий",
      "call me":"Связаться со мной",
      "i will call u":"Я свяжусь с Вами, когда и как Вам будет удобно",
      "write":"Записаться на консультацию",
      "success":"Сообщение успешно отправлено",
      "i will call u i the nearest":"Я свяжусь с Вами в близжайшее время.",
      "sorry":"Извините, что-то пошло не так.",
      "please fill up":"Пожалуйста, заполните все поля правильно и попробуйте еще раз.",
      "please fill up all":"Пожалуйста заполните все поля:",
      "close":"Закрыть",
      "5":"Отлично",
      "4":"Хорошо",
      "3":"Удовлетворительно",
      "2":"Плохо",
      "1":"Очень плохо",
      "comment ok":"Отзыв успешно добавлен, спасибо.",
      "comment ok reload":"Перезагрузите страницу, чтобы увидеть его.",
    },
  }
  </i18n>


<style scoped>
/*--------------------------------------------------------------
# Diplomas
--------------------------------------------------------------*/
.testimonials .testimonials-carousel,
.testimonials .testimonials-slider {
  overflow: hidden;
}

.testimonials .testimonial-item {
  box-sizing: content-box;
  padding: 30px 30px 30px 60px;
  margin: 30px 10px 30px 50px;
  min-height: 200px;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.08);
  position: relative;
  background: #fff;
}

.testimonials .testimonial-item .testimonial-img {
  width: 90px;
  border-radius: 10px;
  border: 6px solid #fff;
  position: absolute;
  left: -45px;
}

.testimonials .testimonial-item h3 {
  font-size: 18px;
  font-weight: bold;
  margin: 10px 0 5px 0;
  color: #111;
}

.testimonials .testimonial-item h4 {
  font-size: 14px;
  color: #999;
  margin: 0;
}

.testimonials .testimonial-item .quote-icon-left,
.testimonials .testimonial-item .quote-icon-right {
  color: #e8ecf5;
  font-size: 26px;
}

.testimonials .testimonial-item .quote-icon-left {
  display: inline-block;
  left: -5px;
  position: relative;
}

.testimonials .testimonial-item .quote-icon-right {
  display: inline-block;
  right: -5px;
  position: relative;
  top: 10px;
}

.testimonials .testimonial-item p {
  font-style: italic;
  margin: 15px auto 15px auto;
}

.testimonials .swiper-pagination {
  margin-top: 20px;
  position: relative;
}

.testimonials .swiper-pagination .swiper-pagination-bullet {
  width: 12px;
  height: 12px;
  background-color: #fff;
  opacity: 1;
  border: 1px solid #5777ba;
}

.testimonials .swiper-pagination .swiper-pagination-bullet-active {
  background-color: #5777ba;
}


/*--------------------------------------------------------------
# About
--------------------------------------------------------------*/
.about .content h3 {
  font-weight: 700;
  font-size: 26px;
  color: #173b6c;
}

.about .content ul {
  list-style: none;
  padding: 0;
}

.about .content ul li {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
}

.about .content ul strong {
  margin-right: 10px;
}

.about .content ul i {
  font-size: 16px;
  margin-right: 5px;
  color: #149ddd;
  line-height: 0;
}

.about .content p:last-child {
  margin-bottom: 0;
}

.comment-box{
  margin-left: 13%;
}

.block-heading {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-bottom: 40px;
}

body{
  background-color:rgba(255, 239, 213, 0.856);
}

.select_language {
    display: flex;
    flex-direction:column-reverse;
    align-items:flex-end;
    padding-top: 120px;
}

</style>