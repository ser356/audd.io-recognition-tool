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
                                <input type="text" class="form-control form-control-lg" v-model="token" />
                            </div>
                        </div>
                        <hr class="mx-n3">
                        <div class="row align-items-center py-3">
                            <div class="col-md-3 ps-5">
                                <h6 class="mb-0">Sample a Analizar</h6>
                            </div>
                            <div class="col-md-9 pe-5">
                                <FileDropComponent @update:files="handleFilesUpdate" />
                            </div>
                        </div>
                        <hr class="mx-n3">
                        <div class="form-check form-switch">
                            <input class="form-check-input" type="checkbox" id="spotifysearch" v-model="spotifysearch">
                            <label class="form-check-label" for="spotifysearch">Buscar en Spotify</label>
                        </div>
                        <div class="form-check form-switch">
                            <input class="form-check-input" type="checkbox" id="applesearch" v-model="applesearch">
                            <label class="form-check-label" for="applesearch">Buscar en Apple Music</label>
                        </div>
                        <hr class="mx-n3">
                        <div class="row d-flex px-5 py-4 justify-content-center align-items-center">
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
    components: {
        FileDropComponent
    },
    data() {
        return {
            token: '',
            spotifysearch: true,
            applesearch: false,
            files: null
        };
    },
    methods: {
        handleFilesUpdate(newFiles) {
            // convert to blob
            const file = newFiles[0];
            const reader = new FileReader();
            reader.onload = (e) => {
                const audioBlob = new Blob([e.target.result], { type: file.type });
                this.files = new File([audioBlob], file.name, { type: file.type });
            };
            reader.onerror = (e) => {
                console.error(e);
            };
            reader.readAsArrayBuffer(file);

        },
        sendForm() {
            
            if (!this.spotifysearch && !this.applesearch) {
                alert('Debes seleccionar al menos una opción');
                return;
            }

            let options = ["spotify", "apple_music"];
            let selectedOption = this.spotifysearch && this.applesearch ? options : this.spotifysearch ? options[0] : options[1];


            let formData = new FormData();
            formData.append('token', this.token);
            formData.append('search', selectedOption);
            formData.append('file', this.files); 
            

            fetch('http://127.0.0.1:5000/api', {
                method: 'POST',
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        }
    }
}
</script>

<style scoped>
.btn {
    border-radius: 20px;
}
</style>
