<template>
    <div class="popup">
        <div class="popup-inner">
            <slot />
            
            <button class="btn btn-primary btn-xl text-uppercase" @click="TogglePopupClient">Close</button>
                          
        </div>
    </div>
</template>

<script>

    export default {
        name: "Popupclient",

        props: ['TogglePopupClient'],

        data() {
          return {

          }
      },
      methods: {
        
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