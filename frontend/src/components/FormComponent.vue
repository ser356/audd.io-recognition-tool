<template>
    <div class="container-fluid h-90" id="formulario">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-xl-9">


                <div class="card mt-3" style="border-radius: 15px;">
                    <div class="card-body">

                        <div class="row align-items-center pt-4 pb-3">
                            <div class="col-md-3 ps-5">

                                <h6 class="mb-0">API Token</h6>

                            </div>
                            <div class="col-md-9 pe-5">

                                <input type="text" class="form-control form-control-lg" v-bind="token" />

                            </div>
                        </div>

                        <hr class="mx-n3">






                        <div class="row align-items-center py-3">
                            <div class="col-md-3 ps-5">

                                <h6 class="mb-0">Sample a Analizar</h6>

                            </div>
                            <div class="col-md-9 pe-5">

                                <FileDropComponent />

                            </div>
                        </div>
                        <hr class="mx-n3">

                        <div class="form-check form-switch">
                            <input class="form-check-input" type="checkbox" id="spotifysearch" v-model="spotifysearch">
                            <label class="form-check-label" for="flexSwitchCheckDefault">Buscar en Spotify</label>
                        </div>
                        <div class="form-check form-switch">
                            <input class="form-check-input" type="checkbox" id="applesearch" v-model="applesearch">
                            <label class="form-check-label" for="flexSwitchCheckDefault">Buscar en Apple Music</label>
                        </div>
                        <hr class="mx-n3">



                        <div class="row d-flex px-5 py-4 ustify-content-center align-items-center">
                            <button type="button" class="btn btn-dark" @click="sendForm">Buscar</button>
                        </div>

                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import FileDropComponent from '@/components/FileDropComponent.vue';



export default {
    methods: {
        sendForm() {
            if (!this.spotifysearch && !this.applesearch) {
                alert('Debes seleccionar al menos una opción');
            } else {

                let options = ["spotify", "apple_music"];

                fetch('http://127.0.0.1:5000/api', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        url: 'https://audd.tech/example.mp3',
                        return: 'spotify',
                        api_token: "d98a5d6b16469144720ddeb924c4b05a"
                    })
                })
                    .then(response =>
                    
                    // i have to try to get the response from the server but in raw format
                    // then i have to convert it to json and then i have to send it to the next view
                    {
                        console.log("ok")
                        console.log(response.json())
                        
                        
                    }
                    ).catch(error => {
                        console.log(error)
                    });
            }
        }

    },
    name: 'HomeView',
    components: {
        FileDropComponent
    },
    data() {
        return {
            token: undefined,
            spotifysearch: true,
            applesearch: false
        };
    },
}
</script>

<style scoped>
.btn {

    border-radius: 20px;
}
</style>
