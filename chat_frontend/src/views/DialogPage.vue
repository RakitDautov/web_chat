<template>
    <div>
        <div class="container">
            <DialogNav></DialogNav>
        </div>
        <div class="container">
            <div class="message-scr">
                <div v-for="db in dialogdb">
                <div class="row justify-content-end" v-if="ifMe(db.user.username)">
                    <div class="col-10">
                        <div class="row justify-content-end">
                            <div class="col-auto">
                                <div class="message my-text text-break" >
                                    <p class="mes-text lh-sm fw-normal">
                                        {{db.text}}
                                    </p>
                                    <div class="text-end lh-1">
                                        <small class="date-text">{{db.date}}</small>
                                        <b-icon icon="check-all"></b-icon>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-start" v-else>
                    <div class="col-10">
                        <div class="row">
                            <div class="col-auto">
                                <div class="message text-break">
                                    <p class="mes-text fw-bolder">{{db.user.username}}</p>
                                    <p class="mes-text lh-sm fw-normal">{{db.text}}</p>
                                    <div class="text-end lh-1">
                                        <small class="date-text">{{db.date}}</small>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-for="dialog in dialogs">
                <div class="row justify-content-end" v-if="ifMe(dialog.username)">
                    <div class="col-10">
                        <div class="row justify-content-end">
                            <div class="col-auto">
                                <div class="message my-text text-break" >
                                    <p class="mes-text lh-sm fw-normal">
                                        {{dialog.message}}
                                    </p>
                                    <div class="text-end lh-1">
                                        <small class="date-text">{{getLocaleTime()}}</small>
                                        <b-icon v-if="checAll" icon="check-all"></b-icon>
                                        <b-icon v-else icon="check"></b-icon>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-start" v-else>
                    <div class="col-10">
                        <div class="row">
                            <div class="col-auto">
                                <div class="message text-break">
                                    <p class="mes-text fw-bolder">{{dialog.username}}</p>
                                    <p class="mes-text lh-sm fw-normal">{{dialog.message}}</p>
                                    <div class="text-end lh-1">
                                        <small class="date-text">{{getLocaleTime()}}</small>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            </div>
            <div>
                <div class="input-group">
                    <input class="text form-control" v-model="form.textarea" placeholder="Сообщение...">
                    <button type="button" class="btn btn-secondary" @click="sendMes">
                        <b-icon icon="arrow-right-square"></b-icon>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import DialogNav from '@/components/DialogNav.vue'

export default {
        name: "dialogpage",
        components: {
            DialogNav
        },
        data() {
            return {
                dialogs: [],
                dialogdb: [],
                form: {
                    textarea: '',
                },
                chatSocket: '',
                checAll: false,
            }
        },
        created() {
            this.connect()
        },
        mounted() {
             this.loadDialog()
        },
        methods: {
            // Подключение сокета
            connect() {
                this.chatSocket = new WebSocket(
                    'ws:' + '127.0.0.1:8000/ws/chat/' + this.$route.params.id + '/');
                this.chatSocket.onopen = () => {
                    this.chatSocket.onmessage = ({data}) => {
                        this.dialogs.push(JSON.parse(data));
                    };
                };
            },

            // Загрузка диалога
            loadDialog() {
                fetch("http://127.0.0.1:8000/chat/?room=" + this.$route.params.id, {
                    method: 'GET',
                    headers: {
                        'Authorization': "Token " + sessionStorage.getItem('auth_token'),
                    },
                })
                    .then(response => response.json())
                    .then(response => {
                        this.dialogdb = response.data.data
                    })
            },
            // Возвращает true если сообщеиния авторизованного пользователя
            ifMe(name) {
                return sessionStorage.getItem('username') == name
            },
            // Отправка сообщения
            sendMes(e) {
                this.saveMes();
                this.chatSocket.send(JSON.stringify({
                    'message': this.form.textarea, 'username': sessionStorage.getItem("username")
                }));
                this.form.textarea = "";
            },

            // Сохранение сообщения в бд
            saveMes() {
                fetch("http://127.0.0.1:8000/chat/", {
                    method: "POST",
                    headers: {
                        'Authorization': "Token " + sessionStorage.getItem('auth_token'),
                        'Accept': 'application/json, text/plain, */*',
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        room: this.$route.params.id,
                        text: this.form.textarea,
                    })
                })
                .then(response => {
                    if (response.status === 201) {
                        this.checAll=true
                    };
                })
                .catch(error => alert(error.statusText))
            },
            // Текущее время пользователя
            getLocaleTime() {
                var dateWithouthSecond = new Date();
                return dateWithouthSecond.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
            },
        }
    }   
</script>


<style scoped>
.container {
  border: 1px solid #dedede;
  background-color: #f8f9fa;
  padding: 1%;
  margin: 0%;
  overflow: hidden;
}
.message {
  background-color: #eae6e6;
  border-radius: 5px;
  padding: 8px;
  margin: 3px;
}
.mes-text {
    padding: 0px;
    margin: 0px;
}
.my-text {
    background-color: rgb(99, 99, 239);
    color: white;
}
.date-text {
    font-size: 80%;
}
.message-scr {
    height: 500px;
    overflow-y: scroll;
    overflow-x: hidden;
}
</style>