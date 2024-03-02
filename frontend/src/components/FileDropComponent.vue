<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
    name: 'FileDropComponent',
    emits: ['files-added'],
    setup(props, { emit }) {
        const fileInput = ref<HTMLInputElement | null>(null);

        const handleDragOver = (event: DragEvent) => {
            event.preventDefault();
        };

        const handleDrop = (event: DragEvent) => {
            event.preventDefault();
            if (event.dataTransfer) {
                const files = event.dataTransfer.files;
                processFiles(files);
            }
        };

        const handleFiles = (event: Event) => {
            const input = event.target as HTMLInputElement;
            if (input.files) {
                processFiles(input.files);
            }
        };

        const processFiles = (files: FileList) => {
            emit('files-added', files);
        };

        const openFileChooser = () => {
            fileInput.value?.click();
        };

        return { handleDragOver, handleDrop, handleFiles, openFileChooser, fileInput };
    },
});
</script>

<template>
    <div class="file-drop-area border-dashed border-3 border-primary p-5" @dragover.prevent="handleDragOver"
        @drop.prevent="handleDrop" @click="openFileChooser">
        <p class="text-center">Arrastra tus archivos aquí o haz clic para seleccionar archivos</p>
        <input type="file" multiple @change="handleFiles" class="d-none" ref="fileInput">
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
