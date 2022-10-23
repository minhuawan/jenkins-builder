using System.IO;
using UnityEngine;

namespace EditorBuild.PostProcessor
{
    public class PostProcessBuildWindows
    {
        private static Logger logger = Logger.GetLogger<PostProcessBuildWindows>();

        public void PostProcessBuild(Config config, string pathToBuiltProject)
        {
            // 0. 检测是否为直接打出 exe
            if (!pathToBuiltProject.EndsWith(".exe") || !File.Exists(pathToBuiltProject))
            {
                logger.Log($"ignore {pathToBuiltProject}");
                // ignore
                return;
            }

            var outputPath = Path.GetDirectoryName(pathToBuiltProject);
            foreach (var item in config.postBuildCopyItems)
            {
                var key = item.key;
                logger.Log($"PostProcessBuild key `{key}`");
                if (!Directory.Exists(item.src))
                {
                    logger.Error($"item.src `{item.src}` not existed");
                    continue;
                }

                var destPath = Path.Combine(outputPath, item.dest_offset);
                logger.Log($"copy `{item.src}` to `{destPath}`");
                CopyFolder(item.src, destPath);
            }
        }


        private void CopyFolder(string srcFolder, string destFolder)
        {
            if (!Directory.Exists(destFolder))
            {
                Directory.CreateDirectory(destFolder);
            }

            foreach (var item in Directory.EnumerateFiles(srcFolder))
            {
                File.Copy(item, Path.Combine(destFolder, Path.GetFileName(item)), true);
            }

            foreach (var item in Directory.EnumerateDirectories(srcFolder))
            {
                CopyFolder(item, Path.Combine(destFolder, Path.GetFileName(item)));
            }
        }
    }
}