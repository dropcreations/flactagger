# __FLAC Tagger__

- This program is to tag __FLAC__ media files using __Mutagen__.
- __Mutagen__ is a Python module to handle audio metadata and tags.

## __Installation__

1) First clone the repo.
```shell
git clone https://github.com/dropcreations/FLAC_Tagger.git && cd FLAC_Tagger
```
2) Install `mutagenFLAC`.
```shell
pip install --editable .
```

## __Usage__

- You can add one FLAC file at once.

```shell
mutagenFLAC [FLAC_path]
```

## __Explanation__

- You can add multiple values to a tag by seperating it with a comma and a space (', ').

    `eg : Tag_Value_01, Tag_Value_02, Tag_Value_03,...`

- When you are adding lyrics, first save lyrics to a text file.
- Then add that text file's path when it asked.
- You can add more custom tags.
- Save all custom tags to text file or type one by one while running.
- If you are using a text file to add custom tags, text file's format must be as below.

    `Tag_Name_01: Tag_Value_01, Tag_Value_02, Tag_Value_03,...`<br>
    `Tag_Name_02: Tag_Value_01, Tag_Value_02, Tag_Value_03,...`

    eg:

    ![CustomTagsPreview](https://raw.githubusercontent.com/dropcreations/FLAC_Tagger/main/CustomTags_Preview.png)

- You can add covers/albumarts. (PNG and JPG/JPEG are supported)
