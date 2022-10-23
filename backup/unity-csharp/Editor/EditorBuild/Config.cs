using System;
using System.Collections.Generic;

namespace EditorBuild
{
    public class Config
    {
        [Serializable]
        public class PostBuildCopyItem
        {
            public string key;
            public string src;
            public string dest_offset;
        }

        public List<PostBuildCopyItem> postBuildCopyItems;
    }
}