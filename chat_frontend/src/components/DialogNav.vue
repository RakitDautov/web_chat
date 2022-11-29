<template>
    <nav class="navbar">
        <div class="container">
            <div class="row justify-content-start">
                <button type="button" class="btn btn-light" @click="goHome()">
                    <b-icon icon="house"></b-icon>
                </button>
            </div>
            <div class="row justify-content-center">
                <div class="col-auto">
                    <div class="text-center">
                        {{room_name}} комната <br>
                        <small>{{count_users}} участников</small>
                    </div>
                </div>
            </div>
            <div class="row justify-content-end">
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
    export default {
        name: "dialognav",
        data() {
            return {
                room_name: "",
                count_users: ""
            }
        },
        created() {
            this.loadRoom()
        },
        methods: {
            // Загрузка сообщений
            loadRoom() {
                fetch("http://127.0.0.1:8000/room/", {
                    method: 'GET',
                    headers: {
                        'Authorization': "Token " + sessionStorage.getItem('auth_token'),
                    },
                })
                    .then(response => response.json())
                    .then(response => {
                        this.room_name = response.data.data.find(item => item.id == this.$route.params.id).name
                        this.count_users = Object.keys(response.data.data.find(
                            item => item.id == this.$route.params.id).invited).length
                        console.log(this.count_users)
                    })
            },
            logout(){
                sessionStorage.removeItem('auth_token')
                window.location = '/'
            },
            goHome() {
                window.location = '/'
            }
        }

    }
</script>

<style >
</style>