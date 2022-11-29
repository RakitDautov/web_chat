<template>
    <nav class="navbar">
        <div class="container justify-content-end">
            <div class="row">
                <div class="col-auto">
                    <button type="button" class="btn btn-light" @click="logout">
                        <b-icon icon="box-arrow-in-left"></b-icon>
                    </button>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import Login from '@/components/Login.vue'

export default {
    name: 'home-nav',
    components: {
        Login
    },
    methods: {
      logout(){
        sessionStorage.removeItem('auth_token')
        window.location = '/'
      },
    },
  }
</script>

<style>
</style>