<template>
    <div class="chats-content">
        <table class="table">
            <span class="heading">Выберать / создать комнату</span>
                <hr/>
            <tbody>
                <tr v-for='room in rooms'>
                    <h5 class="lol bg-primary" @click="openDialog(room.id, room.name)">{{room.name}}</h5>
                </tr>
            </tbody>  
        </table>
        <form class="form-inline">
            <div class="input-group">
                <input class="text form-control" v-model="room_name" placeholder="Название комнаты">
                <b-button type="button" variant="primary" @click="addRoom">Создать</b-button>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: "chat",
        data() {
            return {
                rooms: '',
                room_name: ''
            }
        },
        created() {
            this.loadRoom()
        },
        methods: {
            // Загружает список комнат
            loadRoom() {
                fetch("http://127.0.0.1:8000/room/", {
                    method: 'GET',
                    headers: {
                        'Authorization': "Token " + sessionStorage.getItem('auth_token'),
                    },
                })
                    .then(response => response.json())
                    .then(response => {
                        this.rooms = response.data.data
                    })
            },
            // Открыть диалог
            openDialog(id, name) {
                this.$router.push({name: 'dialogpage', params: {id: id}})
            },
            // Добавить комнату
            addRoom() {
                let data = {
                    name: this.room_name,
                }
                fetch("http://127.0.0.1:8000/room/", {
                    method: 'POST',
                    headers: {
                        'Authorization': "Token " + sessionStorage.getItem('auth_token'),
                        'Accept': 'application/json, text/plain, */*',
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                })
                .then(response => response.json())
                .then(response => {
                    this.loadRoom()
                })
                this.room_name = ''
            }
        }
    }
</script>

<style scoped>
.chats-content {
    margin: auto;
    background: rgb(245, 241, 241);
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    border: 2px solid #dedede;
}
.lol {
    margin: 1px;
    border-radius: 8px;
    text-align: left;
    color: white;
}
.heading{
    font-size: 150%;
}
</style>