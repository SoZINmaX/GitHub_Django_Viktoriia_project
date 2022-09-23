<template>
  <body id="page-top" data-bs-spy="scroll" data-bs-target="#mainNav" data-bs-offset="54">
  <header class="masthead" >
      <div class="container">
          <div class="intro-text">
              <div class="intro-lead-in"><span>Welcome To Our Studio!</span></div>
              <div class="intro-heading text-uppercase"><span>It's Nice To Meet You</span></div><a class="btn btn-primary btn-xl text-uppercase" role="button" href="#about">Tell mE more</a>
          </div>
      </div>
  </header>
  <!-- ======= About Section ======= -->
  <section id="about" class="about">
      <div class="container">

        <div class="section-title">
          <h2>About</h2>
          <p>Magnam dolores commodi suscipit. Necessitatibus eius consequatur ex aliquid fuga eum quidem. Sit sint consectetur velit. Quisquam quos quisquam cupiditate. Et nemo qui impedit suscipit alias ea. Quia fugiat sit in iste officiis commodi quidem hic quas.</p>
        </div>

        <div class="row">
          <div class="col-lg-4" data-aos="fade-right">
            <img src="src/assets/assets/img/image_1.jpg" class="img-fluid" alt="">
          </div>
          <div class="col-lg-8 pt-4 pt-lg-0 content" data-aos="fade-left">
            <h3>UI/UX Designer &amp; Web Developer.</h3>
            <p class="fst-italic">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
              magna aliqua.
            </p>
            <div class="row">
              <div class="col-lg-6">
                <ul>
                  <li><i class="bi bi-chevron-right"></i> <strong>Birthday:</strong> <span>1 May 1995</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>Website:</strong> <span>www.example.com</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>Phone:</strong> <span>+123 456 7890</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>City:</strong> <span>New York, USA</span></li>
                </ul>
              </div>
              <div class="col-lg-6">
                <ul>
                  <li><i class="bi bi-chevron-right"></i> <strong>Age:</strong> <span>30</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>Degree:</strong> <span>Master</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>PhEmailone:</strong> <span>email@example.com</span></li>
                  <li><i class="bi bi-chevron-right"></i> <strong>Freelance:</strong> <span>Available</span></li>
                </ul>
              </div>
            </div>
            <p>
              Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis.
              Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.
            </p>
          </div>
        </div>

      </div>
    </section><!-- End About Section -->
  <section id="portfolio" class="clean-block slider dark" style="margin-bottom: -1px;">
      <div class="container">
          <div class="block-heading">
              <h2 class="text-info">Diplomas</h2>
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
  <section id="review">
    <div class="container">
          <div class="block-heading">
              <h2 class="text-info">Comments</h2>
          </div>
          <div class="carousel slide" data-bs-ride="carousel" id="carousel-2">
              <div class="carousel-inner">
                  <div class="carousel-item active">
                    <div class="d-flex media">
              <div class="media-body">
                  <h4>Love this!</h4>
                  <div>
                    <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star-half"></i>
                  </div>
                  <p v-for="comment in comments">{{ comment.comment }}</p>
                  <p><span class="reviewer-name"><strong>John Doe</strong></span><span class="review-date">7 Oct 2015</span></p>
                  <h4>Love this!</h4>
                  <div>
                    <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star-half"></i>
                  </div>
                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis maximus nisl ac diam feugiat, non vestibulum libero posuere. Vivamus pharetra leo non nulla egestas, nec malesuada orci finibus. </p>
                  <p><span class="reviewer-name"><strong>John Doe</strong></span><span class="review-date">7 Oct 2015</span></p>
                  </div>
              </div>
          </div>
              <div class="carousel-item">
                  <div class="d-flex media">
                    <div class="media-body">
                      <h4>Fantastic product</h4>
                        <div><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis maximus nisl ac diam feugiat, non vestibulum libero posuere. Vivamus pharetra leo non nulla egestas, nec malesuada orci finibus. </p>
                        <p><span class="reviewer-name"><strong>Jane Doe</strong></span><span class="review-date">7 Oct 2015</span></p>
                        <h4>Fantastic product</h4>
                        <div><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis maximus nisl ac diam feugiat, non vestibulum libero posuere. Vivamus pharetra leo non nulla egestas, nec malesuada orci finibus. </p>
                        <p><span class="reviewer-name"><strong>Jane Doe</strong></span><span class="review-date">7 Oct 2015</span></p>
                      </div>
                  </div>
               </div>
              <div class="carousel-item">
                  <div class="d-flex media">
                      <div class="media-body">
                        <h4>Fantastic product</h4>
                        <div><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis maximus nisl ac diam feugiat, non vestibulum libero posuere. Vivamus pharetra leo non nulla egestas, nec malesuada orci finibus. </p>
                        <p><span class="reviewer-name"><strong>Jane Doe</strong></span><span class="review-date">7 Oct 2015</span></p>
                        <h4>Fantastic product</h4>
                        <div><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis maximus nisl ac diam feugiat, non vestibulum libero posuere. Vivamus pharetra leo non nulla egestas, nec malesuada orci finibus. </p>
                        <p><span class="reviewer-name"><strong>Jane Doe</strong></span><span class="review-date">7 Oct 2015</span></p>
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
      </div>
  </section>
  <section class="py-5"></section>
  <section id="contact">
      <div class="container">
          <div class="row">
              <div class="col-lg-12 text-center">
                  <h2 class="text-uppercase section-heading">Contact Us</h2>
                  <h3 class="text-muted section-subheading">Lorem ipsum dolor sit amet consectetur.</h3>
              </div>
          </div>
          <div class="row">
              <div class="col-lg-12">
                  <form id="contactForm" name="contactForm" novalidate="novalidate">
                      <div class="row">
                          <div class="col-md-6">
                              <div class="form-group mb-3"><input class="form-control" type="text" id="name" placeholder="Your Name *" required=""><small class="form-text text-danger flex-grow-1 help-block lead"></small></div>
                              <div class="form-group mb-3"><input class="form-control" type="email" id="email" placeholder="Your Email *" required=""><small class="form-text text-danger help-block lead"></small></div>
                              <div class="form-group mb-3"><input class="form-control" type="tel" placeholder="Your Phone *" required=""><small class="form-text text-danger help-block lead"></small></div>
                          </div>
                          <div class="col-md-6">
                              <div class="form-group mb-3"><textarea class="form-control" id="message" placeholder="Your Message *" required=""></textarea><small class="form-text text-danger help-block lead"></small></div>
                          </div>
                          <div class="w-101"></div>
                          <div class="col-lg-12 text-center">
                              <div id="success"></div><button class="btn btn-primary btn-xl text-uppercase" id="sendMessageButton" type="submit">Send Message</button>
                          </div>
                      </div>
                  </form>
              </div>
          </div>
      </div>
  </section>
  <footer>
      <div class="container">
          <div class="row">
              <div class="col-md-12">
                  <ul class="list-inline social-buttons">
                      <li class="list-inline-item"><a href="#"><i class="fa fa-twitter"></i></a></li>
                      <li class="list-inline-item"><a href="#"><i class="fa fa-facebook"></i></a></li>
                      <li class="list-inline-item"><a href="#"><i class="fa fa-linkedin"></i></a></li>
                  </ul>
              </div>
          </div>
      </div>
  </footer>
</body>
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
      const response = await fetch('api/v1/comment/list_add/')
      if (response.status === 200){
          this.comments = await response.json()
      }
  }
}
</script>
<style scoped>
/*--------------------------------------------------------------
# Testimonials
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

.img-fluid {
  max-height: 390px;
}

</style>