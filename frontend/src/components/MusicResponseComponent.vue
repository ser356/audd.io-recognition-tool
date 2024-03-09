<template>
    <div class="music-cards-container">
        <div v-if="responseData.result.spotify" class="music-card card">
            <img class="card-img-top" :src="spotifyImageUrl" alt="Album Cover Spotify">
            <div class="card-body">
                <h5 class="card-title">{{ responseData.result.title }}</h5>
                <p class="card-text">{{ responseData.result.artist }}</p>
                <div>
                    
                    <a :href="responseData.result.spotify.external_urls.spotify" target="_blank" class="btn btn-dark">Escuchar en Spotify </a>
                </div>
               
                
            </div>
            <div class="card-footer">
                <small class="text-muted">{{ responseData.result.timecode }}</small>
            </div>
        </div>

        <div v-if="responseData.result.apple_music" class="music-card card">
            <img class="card-img-top" :src="appleMusicImageUrl" alt="Album Cover Apple Music">
            <div class="card-body">
                <h5 class="card-title">{{ responseData.result.title }}</h5>
                <p class="card-text">{{ responseData.result.artist }}</p>
                <a :href="responseData.result.apple_music.url" target="_blank" class="btn btn-dark">Escuchar en Apple Music</a>
            </div>
            <div class="card-footer">
                <small class="text-muted">{{ responseData.result.timecode }}</small>
            </div>
        </div>
    </div>
    <div class="refresh" @click="resetState">
<span>Recargar</span>

        <span class="material-symbols-outlined">
cached
</span>
    </div>
</template>

<script>
export default {
  methods: {
    resetState() {
      // Reset state of the web doing a page refresh
        window.location.reload();
    }
},

    name: 'MusicCards',
    props: {
        responseData: {
            type: Object,
            required: true
        },
    },
    computed: {
        spotifyImageUrl() {
            return this.responseData.result.spotify.album.images[0].url;
        },
        appleMusicImageUrl() {
            let artwork = this.responseData.result.apple_music.artwork;
            return artwork.url.replace('{w}', artwork.width.toString()).replace('{h}', artwork.height.toString());
        }
    }
}
</script>

<style scoped>
.refresh {
    font-size: 2rem;
    margin-left: 40px;
    margin-top: 30px;
    cursor: pointer;
}
.music-cards-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 20px;
    margin-top: 2rem;
}

.music-card {
    width: 18rem; /* Adjust card width as needed */
}
</style>