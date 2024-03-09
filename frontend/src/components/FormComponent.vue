<template>

    <div v-if="responseData===null">
        <ModalAlertComponent :show="triggerModal" @update:show="triggerModal = $event" title="Error">
            <template v-slot:default>
                <p>Debes completar todos los campos requeridos.</p>
            </template>
        </ModalAlertComponent>

        <div class="container-fluid container-sm h-90" id="formulario">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-xl-9">
                    <div class="card mt-3" style="border-radius: 15px;">
                        <div class="card-body">
                            <div class="row align-items-center pt-4 pb-3">
                                <div class="col-md-3 ps-5">
                                    <h6 class="mb-0">API Token</h6>
                                </div>
                                <div class="col-md-9 pe-5">
                                    <input type="password" class="form-control form-control-lg" v-model="token" />
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
    </div>
<MusicResponseComponent v-if="responseData !== null" :responseData="responseData" />

</template>

<script>
import FileDropComponent from '@/components/FileDropComponent.vue';
import MusicResponseComponent from '@/components/MusicResponseComponent.vue'; // Asegúrate de tener este componente
import ModalAlertComponent from './ModalAlertComponent.vue';

export default {
    components: {
        FileDropComponent,
        MusicResponseComponent,
        ModalAlertComponent
    },
    data() {
        return {
            token: '',
            spotifysearch: false,
            applesearch: false,
            files: null,
            responseData: null,
            triggerModal: false
        };
    },
    methods: {
        handleFilesUpdate(newFiles) {
            const file = newFiles[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const audioBlob = new Blob([e.target.result], { type: file.type });
                    this.files = new File([audioBlob], file.name, { type: file.type });
                };
                reader.onerror = (e) => {
                    console.error(e);
                };
                reader.readAsArrayBuffer(file);
            }
        },
        sendForm() {
            if (!this.token || !this.files || (!this.spotifysearch && !this.applesearch)) {
                this.triggerModal = true;
                return;
            }

            let selectedOption = this.spotifysearch && this.applesearch ? ["spotify","apple_music"] : this.spotifysearch ? "spotify" : "apple_music";

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
                    this.responseData = data;
                })
                .catch((error) => {
                    console.error('Error:', error);
                    this.triggerModal = true;
                });
        }
    }
}
</script>

<style scoped>
.btn {
    border-radius: 20px;
}

.card-body {
    padding: 3rem 4rem;
    /* Reduce el relleno horizontal del cuerpo de la tarjeta */
}

.row.align-items-center {
    margin-bottom: 0.5rem;
    /* Reduce el margen inferior de las filas */
}

hr.mx-n3 {
    margin-top: 0.5rem;
    /* Reduce el margen superior de los separadores */
    margin-bottom: 0.5rem;
    /* Reduce el margen inferior de los separadores */
}

.form-check.form-switch {
    margin-bottom: 0.5rem;
    /* Reduce el margen inferior de los interruptores */
}
</style>