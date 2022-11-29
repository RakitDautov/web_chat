<template>
    <div class="login-content">
        <form @submit.prevent class="form-horizontal">
            <span class="heading text-center">Авторизация</span>
            <hr/>
            <div class="form-group">
                <input class="form-control" v-model="login" placeholder="Логин" type="text"/>
            </div>
            <div class="form-group">
                <input class="form-control" v-model="password" placeholder="Пароль" type="password"/>
            </div>
            <div>
                <b-button type="submit" variant="primary" @click="setLogin">Вход</b-button>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: "login",
        data() {
            return {
                login: "",
                password:""
            }
        },
        methods: {
            setLogin() {
                // Авторизация пользователя
                let data = {
                    username: this.login,
                    password: this.password
                }
                fetch("http://127.0.0.1:8000/auth/token/login/", {
                    method: "POST",
                    headers: {
                        'Accept': 'application/json, text/plain, */*',
                        'Content-Type': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                    body: JSON.stringify(data),
                })
                .then(response => {
                    if (response.status === 200) {
                        return response.json()
                    } else if (response.status === 400) {
                        alert("Логин или пароль не верен")
                    } else alert(response.text());
                })
                .then(response => {
                    sessionStorage.setItem("auth_token", response.data.attributes.auth_token);
                    sessionStorage.setItem("username", this.login);
                    window.location = '/'
                })
            },
        },
    }
</script>


<style scoped>
.heading{
    text-align: center;
    font-size: 180%;
}
.form-control{
    margin: 5px;
    padding: 10px;
    border: 2px solid #dedede;
    display: flex;
    justify-content: center;
}
.login-content {
    margin: auto;
    background: rgb(245, 241, 241);
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    border: 2px solid #dedede;
    margin-top: 80px;
}
</style>