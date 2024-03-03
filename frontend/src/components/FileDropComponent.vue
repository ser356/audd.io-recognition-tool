<script lang="ts">
import { defineComponent, ref, onMounted, watch } from 'vue';

export default defineComponent({
    name: 'FileDropComponent',
    emits: ['files-added', 'error', 'update:files'],
    props: {
        initialFiles: {
            type: FileList,
            default: () => null,
        },
    },
    setup(props, { emit }) {
        const fileInput = ref<HTMLInputElement | null>(null);
        const files = ref<FileList | null>(null);

        const handleDragOver = (event: DragEvent) => {
            event.preventDefault();
        };

        const handleDrop = (event: DragEvent) => {
            event.preventDefault();
            if (event.dataTransfer) {
                const filesDropped = event.dataTransfer.files;
                processFiles(filesDropped);
            }
        };

        const handleFiles = (event: Event) => {
            const input = event.target as HTMLInputElement;
            if (input.files) {
                processFiles(input.files);
            }
        };

        const processFiles = (filesInput: FileList) => {
            if (filesInput.length > 0) {
                const allowedTypes = ['audio/mp3', 'audio/mpeg'];
                for (let i = 0; i < filesInput.length; i++) {
                    if (!allowedTypes.includes(filesInput[i].type)) {
                        emit('error', 'Only MP3 files are allowed');
                        return;
                    }
                }
                files.value = filesInput;
                emit('files-added', filesInput);
                emit('update:files', filesInput); // Emit update:files event
            }
        };

        const openFileChooser = () => {
            fileInput.value?.click();
        };

        onMounted(() => {
            if (props.initialFiles) {
                processFiles(props.initialFiles);
            }
        });

        watch(() => props.initialFiles, (newFiles) => {
            if (newFiles) {
                processFiles(newFiles);
            }
        });

        return { handleDragOver, handleDrop, handleFiles, openFileChooser, fileInput, files };
    },
});
</script>

<template>
    <div class="file-drop-area border-dashed border-3 border-primary p-5" @dragover.prevent="handleDragOver"
        @drop.prevent="handleDrop" @click="openFileChooser">
        <p class="text-center" v-if="!files || files.length === 0">
            Arrastra tus archivos aquí o haz clic para seleccionar archivos. Solo se permiten archivos MP3.
        </p>
        <p class="text-center" v-else>
            Archivo seleccionado: {{ files[0]?.name }}
        </p>
        <input type="file" multiple @change="handleFiles" class="d-none" ref="fileInput" accept=".mp3">
    </div>
</template>

<style scoped>
.file-drop-area {
    border-radius: 20px;
    cursor: pointer;
}

.file-drop-area:hover {
    background-color: #f8f9fa;
}
</style>
