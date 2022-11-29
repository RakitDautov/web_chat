<template>
  <div>
    <div v-if="auth">
      <div>
          <home-nav/>
      </div>
      <div>
        <chats/>
      </div>
    </div>
    <div v-else>
      <div>
        <login/>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import Chats from '@/components/Chats.vue'
  import Login from '@/components/Login.vue'
  import HomeNav from '@/components/HomeNav.vue'
  
  export default {
      name: 'HomePage',
      computed: {
        auth() {
          if (sessionStorage.getItem('auth_token')) {
            return true 
          }
        },
      },
      components: {
          Chats,
          Login,
          HomeNav
      },
    }
  </script>
  
  <style>
  
  </style>